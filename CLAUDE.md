# sensebar-agent-knowledge-vault-builder

## 知識庫查詢規則

涉及下列主題時，**必須先查閱 `Clipping/` 內的逐字稿檔**，再根據內容回答，不得憑空推測：

- 三師爸的意見、觀點、評論
- 三師爸的教學方法、工作流程
- @sensebar 頻道影片中的具體內容
- 三師爸對特定工具（Claude、Codex、AntiGravity、OpenCode 等）的評價

## 聲音克隆

需要以三師爸的聲音回答時，使用 `..\voxcpm_clone.py` 進行推論：

- 參考音檔：`..\ref_voice.wav`
- 範例輸出：`..\clone_demo.wav`、`..\ultimate_clone.wav`

## 資料夾結構

| 路徑 | 用途 |
|------|------|
| `Clipping/` | YouTube 字幕原始逐字稿（不修改） |
| `創作庫/` | 自訂教材、講義、腳本 |
| `知識庫/` | Agent 管理的結構化知識 |
| `extract_videos.py` | 掃描 @sensebar 頻道影片+直播，過濾 AI 相關影片 |
| `download_all_subs.py` | 下載字幕並去重清理，存入 Clipping/ |

## 資料來源

- 頻道：[@sensebar](https://www.youtube.com/@sensebar)
- 過濾關鍵字：claude, codex, antigravity, opencode, agent, googlea
- 目前收錄：66 支影片（含 21 支直播；直播無字幕者不入 Clipping/）
