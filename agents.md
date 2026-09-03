# agents.md — 給 Codex / OpenCode 等 Agent 的入口

本 repo 的 Agent 指引以 **`CLAUDE.md`** 為準（知識庫查詢規則、資料夾結構、資料來源、聲音克隆），請先讀它；`README.md` 則是完整的建置流程說明。本檔只補充跨平台差異與最小操作摘要。

## 一句話說明

用 Agent 把 YouTube 頻道 @sensebar 的 AI 相關影片字幕抓下來、清成可讀逐字稿，存進 `Clipping/`，再由 Agent 整理成 `知識庫/` 的結構化筆記。

## 操作摘要（細節見 README.md）

```bash
pip install yt-dlp
python extract_videos.py       # 掃頻道 → sensebar_ai_urls.txt（+ sensebar_ai_videos.md / sensebar_all_videos.md）
python download_all_subs.py    # 依 urls 下載字幕、去重清理 → Clipping/*.md
```

| 資料夾 | 角色 | 可否修改 |
|--------|------|----------|
| `Clipping/` | 原始逐字稿（外部來源） | 只讀，不修改 |
| `創作庫/` | 三師爸自己的教材、講義、腳本 | 只讀，不修改 |
| `知識庫/` | Agent 整理出的結構化知識、索引、紀錄 | Agent 負責維護 |

## 平台差異（Claude Code / Codex / OpenCode）

- Claude Code 會自動讀 `CLAUDE.md`；Codex 與 OpenCode 讀本檔（`agents.md` / `AGENTS.md`），請在開工時自行把 `CLAUDE.md` 讀進來。
- 技能安裝路徑不同：Claude Code `~/.claude/skills/`、Codex `~/.agents/skills/`、OpenCode `~/.config/opencode/skills/`；本 repo 本身不含技能，只有腳本。
- 摘要與整理逐字稿時，用任一支援長文的模型即可；單支影片逐字稿可能超過數萬字，必要時分段處理。
- 排程（每週整理）在各平台做法不同：Claude Code 用排程任務或 `/loop`，Codex / OpenCode 請用系統排程（cron / 工作排程器）觸發。

## 禁止事項

- 不改寫、不刪除 `Clipping/` 與 `創作庫/` 內任何檔案。
- 回答三師爸的觀點或影片內容前，必須先查 `Clipping/`，不得憑空推測。
- 不把 `subtitles/`、`*.vtt`、影音檔加進 git（見 `.gitignore`）。
- 不在 repo 內放 API 金鑰或個人音檔。
