# AI Agent YouTube Subtitle Knowledge Base Builder (Agent-to-Agent Guide)

This repository outlines the automated workflow for AI Agents to extract subtitles from a YouTube channel, parse and clean the transcripts, build a structured three-layer Obsidian Second Brain database, and utilize it for automated lesson/teaching planning.

> [!NOTE]
> This guide is formatted specifically for consumption by agentic AI coders (such as Claude Code, Codex, AntiGravity, OpenCode). If you are an Agent reading this repo, follow the instructions and run the scripts below to replicate the knowledge base construction.

---

## 🗺️ System Architecture

```mermaid
graph TD
    Channel[@sensebar Channel] -->|1. extract_videos.py| VideoList[Filtered Video List & URLs]
    VideoList -->|2. download_all_subs.py| TempVTT[Raw VTT Subtitles]
    TempVTT -->|3. VTT Cleaning Engine| CleanMD[Deduplicated Markdown Files]
    CleanMD -->|4. Obsidian Vault| ThreeLayer[Three-Layer Vault Structure]
    ThreeLayer -->|5. Weekly Agent Task| KB[Structured Knowledge Base]
```

---

## 🛠️ Step-by-Step Implementation Workflow

### Step 1: Filter Channel Videos & Extract URLs
Use the Python script `extract_videos.py` to fetch video metadata from the target YouTube channel, filter them by specific keywords (`claude`, `codex`, `antigravity`, `opencode`, `agent`), and export a plain list of URLs.

* **Script**: `extract_videos.py`
* **Output**: `sensebar_ai_urls.txt`

### Step 2: Download Subtitles & Clean VTT
Use the script `download_all_subs.py` to loop through the extracted URLs, download subtitles using `yt-dlp`, and clean the output.

* **Cleaning Rules implemented in script**:
  1. Remove VTT metadata headers and timestamps (e.g. `00:00:01.000 --> 00:00:03.000`).
  2. Strip HTML/XML tags (e.g. `<c>`, `</c>`, `<00:00:01.000>`).
  3. **Deduplicate scrolling lines**: YouTube auto-captions replicate scrolling text. The script performs consecutive line deduplication to yield readable transcript blocks.
  4. Write clean Markdown files with video titles as H1 and link back to the source YouTube URL.

### Step 3: Establish the Three-Layer Obsidian Vault
Structure the destination Obsidian vault (the Agent's "Second Brain") into three distinct folders:
1. `Clipping/` (External Sources): Store all the generated transcript markdown files here. **Do not modify these raw files.**
2. `創作庫/` (Creation Vault): Store your own scripts, lecture drafts, and original notes here. **Do not modify these raw files.**
3. `知識庫/` (Knowledge Base): Managed entirely by the Agent. This is where structured knowledge, indexes, and theme folders go.

### Step 4: Run Weekly Agent Restructuring (Agent System Prompt)
As an Agent, schedule a recurring task (e.g. every Sunday) to run the **Weekly Knowledge Restructure**:
1. Scan `Clipping/` and `創作庫/` for new files.
2. Digest the transcripts, extracting key summaries, keywords, and topics.
3. Write/append structured notes into the corresponding folders in `知識庫/` (e.g. `AI工作流/`, `教學趨勢/`).
4. Perform a health check (Lint) to identify content contradictions, link errors, or missing cross-references, mapping them in the Obsidian Graph View.
5. Update the global `Index` and `Log` notes to document changes.

### Step 5: Process Teaching Files & Write Plans (Downstream Tasks)
Once the knowledge base is populated:
* **Writing Lesson/Curriculum Plans**: Place the school's plan template and publisher's syllabus in a folder. Instruct the Agent to read both files and automatically merge and fill the template.
* **Auto-Downloading & OCR**: Instruct the Agent to search the web for exam PDFs (e.g. "國中教育會考"), download them, read questions using OCR, and extract them into new study sheets.
* **Web Interactive Cockpit (教學駕駛艙)**: Prompt the Agent to compile the extracted scripts and slides into an interactive HTML page (with embedded videos, timers, draw-boards, and quizzes) and host it publicly on GitHub Pages.

---

## 📄 Scripts in this Repository

The scripts are located at the root of the workspace:
* [extract_videos.py](extract_videos.py)
* [download_all_subs.py](download_all_subs.py)

---

## 🤖 Instructions for the executing Agent
1. Clone this repository.
2. Install Python dependencies: `pip install yt-dlp`.
3. Run `python extract_videos.py` to extract target videos.
4. Run `python download_all_subs.py` to build the `subtitles/` folder.
5. Create the Obsidian folders (`Clipping`, `創作庫`, `知識庫`) and copy the contents of `subtitles/` into `Clipping/`.
6. Initiate your system prompt to maintain the three-layer knowledge vault.
