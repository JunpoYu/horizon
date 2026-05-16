"""Tencent Cloud Developer Community column scraper."""

import json
import logging
from datetime import datetime
from typing import Any, List
from zoneinfo import ZoneInfo

import httpx
from bs4 import BeautifulSoup
from dateutil import parser as date_parser

from .base import BaseScraper
from ..models import ContentItem, SourceType, TencentCloudColumnConfig

logger = logging.getLogger(__name__)


class TencentCloudColumnScraper(BaseScraper):
    """Scraper for Tencent Cloud Developer Community columns."""

    def __init__(self, sources: List[TencentCloudColumnConfig], http_client: httpx.AsyncClient):
        super().__init__({"sources": sources}, http_client)

    async def fetch(self, since: datetime) -> List[ContentItem]:
        items: List[ContentItem] = []

        for source in self.config["sources"]:
            if not source.enabled:
                continue

            items.extend(await self._fetch_column(source, since))

        return items

    async def _fetch_column(
        self,
        source: TencentCloudColumnConfig,
        since: datetime,
    ) -> List[ContentItem]:
        url = f"https://cloud.tencent.com/developer/column/{source.column_id}"

        try:
            response = await self.client.get(
                url,
                follow_redirects=True,
                headers={"User-Agent": "Mozilla/5.0"},
                timeout=60.0,
            )
            response.raise_for_status()

            articles = self._extract_articles(response.text)
            items: List[ContentItem] = []

            for article in articles:
                article_id = article.get("articleId")
                if not article_id:
                    continue

                published_at = self._parse_datetime(
                    article.get("createTime") or article.get("updateTime")
                )
                if not published_at or published_at < since:
                    continue

                article_url = f"https://cloud.tencent.com/developer/article/{article_id}"
                tags = [
                    tag.get("tagName")
                    for tag in article.get("tags", [])
                    if tag.get("tagName")
                ]

                items.append(
                    ContentItem(
                        id=self._generate_id(
                            "tencent_cloud",
                            source.column_id,
                            str(article_id),
                        ),
                        source_type=SourceType.RSS,
                        title=article.get("title") or "Untitled",
                        url=article_url,
                        content=article.get("summary") or "",
                        author=(article.get("author") or {}).get("nickname") or source.name,
                        published_at=published_at,
                        metadata={
                            "feed_name": source.name,
                            "category": source.category,
                            "column_id": source.column_id,
                            "tags": tags,
                        },
                    )
                )

            return items
        except httpx.HTTPError as e:
            logger.warning("Error fetching Tencent Cloud column %s: %r", source.name, e)
        except Exception as e:
            logger.warning("Error parsing Tencent Cloud column %s: %s", source.name, e)

        return []

    def _extract_articles(self, html: str) -> list[dict[str, Any]]:
        soup = BeautifulSoup(html, "html.parser")
        script = soup.find("script", id="__NEXT_DATA__")
        if not script or not script.string:
            return []

        payload = json.loads(script.string)
        return self._find_article_list(payload)

    def _find_article_list(self, value: Any) -> list[dict[str, Any]]:
        if isinstance(value, list) and value and all(isinstance(item, dict) for item in value):
            if any("articleId" in item and "title" in item for item in value):
                return value

        if isinstance(value, dict):
            for child in value.values():
                found = self._find_article_list(child)
                if found:
                    return found
        elif isinstance(value, list):
            for child in value:
                found = self._find_article_list(child)
                if found:
                    return found

        return []

    def _parse_datetime(self, value: str | None) -> datetime | None:
        if not value:
            return None

        dt = date_parser.parse(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=ZoneInfo("Asia/Shanghai"))
        return dt
