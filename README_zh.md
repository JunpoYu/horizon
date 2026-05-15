# Horizon 个人部署仓库

这个仓库是我基于
[Thysrael/Horizon](https://github.com/Thysrael/Horizon)
搭建的个人部署与配置仓库，用于运行 AI 信息聚合和每日速递。

仓库公开是为了让 GitHub Actions 和 GitHub Pages 正常工作。这里不是
Horizon 的官方项目仓库。原项目、文档、issue 和上游开发请访问：

- 原始仓库：[Thysrael/Horizon](https://github.com/Thysrael/Horizon)
- 原作者：[Thysrael](https://github.com/Thysrael)
- 许可证：[MIT License](LICENSE)

原作者版权声明保留在 `LICENSE` 中。

## 这个仓库做什么

当前配置会：

- 抓取我选定的 AI、科研和技术信息源；
- 使用兼容 OpenAI API 的硅基流动模型进行评分和总结；
- 生成中文每日速递；
- 通过 GitHub Actions 定时运行；
- 通过 GitHub Pages 发布结果。

当前公开页面：

- [https://junpoyu.github.io/horizon/](https://junpoyu.github.io/horizon/)

## 当前信息源

- HackerNews 热门内容
- OpenAI Blog、Nature、The Gradient、Stanford AI Lab、Simon Willison、Jay Alammar、Sebastian Raschka、Yang Song 等 RSS
- Karpathy 的 GitHub 动态
- `heejkoo/awesome-diffusion-models` 的 GitHub release
- Telegram `deep_learning_daily`

这个部署中 Reddit 和 Twitter 已禁用。

## 密钥与安全

真实 API key 不保存在这个仓库里。代码中只保存环境变量名，例如：

```text
SILICONFLOW_API_KEY
```

本地运行时，真实 key 放在 `.env` 中；`.env` 已被 Git 忽略。

GitHub Actions 运行时，真实 key 应配置在：

```text
Settings -> Secrets and variables -> Actions
```

需要配置的 secret：

```text
SILICONFLOW_API_KEY
```

GitHub Actions 自带的 `GITHUB_TOKEN` 用于 GitHub API 访问和发布
`gh-pages` 分支，不需要手动创建。

## 本地运行

安装依赖：

```bash
uv sync
```

运行：

```bash
uv run horizon
```

指定时间窗口：

```bash
uv run horizon --hours 48
```

生成结果会写入：

```text
data/summaries/
docs/_posts/
```

这些生成文件不会提交到 `main`，workflow 会把它们发布到 `gh-pages`。

## GitHub Actions

workflow 文件：

```text
.github/workflows/daily-summary.yml
```

当前配置：

- 每天北京时间 08:00 自动运行；
- 支持手动运行并输入 `hours`；
- 将生成页面发布到 `gh-pages` 分支。

手动运行入口：

```text
Actions -> Daily Horizon Summary -> Run workflow
```

## GitHub Pages

Pages 应配置为：

```text
Source: Deploy from a branch
Branch: gh-pages
Folder: / (root)
```

正确访问地址是小写路径：

```text
https://junpoyu.github.io/horizon/
```

## 同步上游

这个仓库保留了 `upstream` 指向原项目。检查上游更新：

```bash
git fetch upstream
git log --oneline main..upstream/main
```

合并上游前需要先审查改动，因为本仓库包含个人部署配置。
