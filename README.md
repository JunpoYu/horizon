# Horizon Personal Deployment

This repository is my personal deployment and configuration of
[Thysrael/Horizon](https://github.com/Thysrael/Horizon), an AI-powered
information aggregation and daily briefing system.

It is published so GitHub Actions and GitHub Pages can run normally. This is
not the official Horizon project repository. For the original project,
documentation, issues, and upstream development, use:

- Original repository: [Thysrael/Horizon](https://github.com/Thysrael/Horizon)
- Original author: [Thysrael](https://github.com/Thysrael)
- License: [MIT License](LICENSE)

The original copyright notice is preserved in `LICENSE`.

## What This Repo Does

This repo is configured to:

- fetch selected AI, research, and technology sources;
- score and summarize items with an OpenAI-compatible SiliconFlow model;
- generate Chinese daily briefings;
- run automatically with GitHub Actions;
- publish generated pages through GitHub Pages.

Current public site:

- [https://junpoyu.github.io/horizon/](https://junpoyu.github.io/horizon/)

## Current Sources

- HackerNews top stories
- RSS feeds such as OpenAI Blog, Nature, The Gradient, Stanford AI Lab, Simon Willison, Jay Alammar, Sebastian Raschka, and Yang Song
- GitHub activity for Karpathy and `heejkoo/awesome-diffusion-models`
- Telegram `deep_learning_daily`

Reddit and Twitter are disabled in this deployment.

## Secrets

Real API keys are not stored in this repository. The code refers to environment
variable names only, for example:

```text
SILICONFLOW_API_KEY
```

For local runs, keys live in `.env`, which is ignored by Git. For GitHub Actions,
keys should be configured under:

```text
Settings -> Secrets and variables -> Actions
```

Required secret:

```text
SILICONFLOW_API_KEY
```

GitHub's built-in `GITHUB_TOKEN` is used by Actions for GitHub API access and
for publishing to the `gh-pages` branch.

## Local Usage

Install dependencies:

```bash
uv sync
```

Run the pipeline:

```bash
uv run horizon
```

Run with a custom time window:

```bash
uv run horizon --hours 48
```

Generated summaries are written to:

```text
data/summaries/
docs/_posts/
```

These generated files are ignored on `main`; the workflow publishes them to
`gh-pages`.

## GitHub Actions

The workflow is defined in:

```text
.github/workflows/daily-summary.yml
```

It currently:

- runs daily at 08:00 Asia/Shanghai;
- supports manual runs with a configurable `hours` input;
- publishes the generated site to the `gh-pages` branch.

To run manually:

```text
Actions -> Daily Horizon Summary -> Run workflow
```

## GitHub Pages

For this repository, GitHub Pages should be configured as:

```text
Source: Deploy from a branch
Branch: gh-pages
Folder: / (root)
```

The correct project URL is lowercase:

```text
https://junpoyu.github.io/horizon/
```

## Upstream Updates

This repository keeps `upstream` pointed at the original project. To inspect or
pull upstream changes:

```bash
git fetch upstream
git log --oneline main..upstream/main
```

Review upstream changes before merging because this repository contains
personal deployment configuration.
