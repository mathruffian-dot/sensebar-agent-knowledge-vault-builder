# 🤖 AI Agent Automated Knowledge Vault Builder (Agent-to-Agent Specification)

> [!IMPORTANT]
> **Instruction for AI Coders & Autonomous Agents (Claude Code, AntiGravity, Codex, OpenCode, Cursor, Windsurf)**:
> If you are an AI Agent reading this repository, follow the execution instructions below step-by-step to replicate, extract, clean, build, and maintain the Three-Layer Obsidian Knowledge Base from YouTube video transcripts.

---

## 🗺️ System Architecture

```mermaid
graph TD
    YouTubeChannel[@sensebar Channel] -->|1. extract_videos.py| VideoList[Filtered Video List & URLs]
    VideoList -->|2. download_all_subs.py| RawSubs[Cleaned Transcript Markdown Files]
    RawSubs -->|3. Establish Vault| ThreeLayer[Three-Layer Vault Structure]
    ThreeLayer -->|Clipping/| RawClipping[Clipping/ - Immutable Raw Transcripts]
    ThreeLayer -->|創作庫/| RawCreation[創作庫/ - Immutable User Drafts]
    ThreeLayer -->|知識庫/| ManagedKB[知識庫/ - Agent-Managed Knowledge]
    ManagedKB -->|4. Agent Execution| Demos[run_demo.py - 5-Stage Agent Demos]
    ManagedKB -->|5. Weekly Schedule| KBGraph[Auto-Growing Obsidian Knowledge Graph]
```

---

## 🛠️ Step-by-Step Agent Execution Workflow

### Step 1: Environment & Dependency Setup
Initialize the Python environment and install required dependencies.

```bash
pip install -r requirements.txt
cp .env.example .env
```

* **`requirements.txt`**: Includes `google-generativeai`, `python-dotenv`, `colorama`, and `yt-dlp`.
* **`.env`**: (Optional) Populate `GEMINI_API_KEY` for live LLM reasoning.

---

### Step 2: Extract & Filter Video Metadata
Run `extract_videos.py` to scan YouTube channel `@sensebar` (videos and live streams) and filter AI-related content using keywords: `["claude", "codex", "antigravity", "opencode", "agent", "googlea"]`.

```bash
python extract_videos.py
```

* **Outputs**:
  - `sensebar_ai_urls.txt`: Plain list of matching YouTube video URLs (1 URL per line, ready for NotebookLM or `download_all_subs.py`).
  - `sensebar_ai_videos.md`: Markdown summary table of filtered videos with direct links.
  - `sensebar_notebooklm_urls.md`: Clean URL list formatted for direct paste into NotebookLM.

---

### Step 3: Auto-Download Subtitles & Clean Transcripts
Run `download_all_subs.py` to iterate through `sensebar_ai_urls.txt`, fetch subtitles via `yt-dlp`, and clean the output into readable Markdown.

```bash
python download_all_subs.py
```

* **Cleaning Engine Rules**:
  1. Strip WEBVTT headers, language flags, and timestamps (`00:00:01.000 --> 00:00:03.000`).
  2. Strip inline XML/HTML tags (e.g. `<c>`, `</c>`).
  3. **Deduplicate scrolling captions**: YouTube auto-captions replicate scrolling text; consecutive identical lines are automatically collapsed.
  4. Write clean Markdown files formatted with Video Title H1 and link back to the source YouTube URL.
  5. Store files into `Clipping/`. Existing transcript files are automatically skipped for resume capability.

---

### Step 4: Establish the Three-Layer Obsidian Vault
Follow the **Andrej Karpathy (卡帕西) LLM Note Management Principle**: *Raw data must remain immutable; the AI Agent actively manages and expands the structured knowledge graph.*

1. **`Clipping/` (External Raw Data)**: Stores raw YouTube transcript Markdown files. **Do not edit raw files.**
2. **`創作庫/` (User Drafts & Creation)**: Stores user-written scripts, lesson plans, and original notes. **Do not edit raw files.**
3. **`知識庫/` (Agent-Managed Vault)**: Managed entirely by the Agent. Contains structured topic notes, cross-reference links, tags, and index files.

---

### Step 5: Test & Run Agent Demonstrations
Run `run_demo.py` to verify the 5 core AI Agent execution stages:

```bash
# Run interactive menu
python run_demo.py

# Or run full 5-stage automated suite
python run_demo.py A
```

* **Stage 1 (`simple_agent.py`)**: ReAct Loop (`Thought -> Action -> Observation`).
* **Stage 2 (`demo_stage2_function_calling.py`)**: Native Function Calling with JSON Schema.
* **Stage 3 (`demo_stage3_memory.py`)**: Conversation Memory & Sliding Window Context.
* **Stage 4 (`demo_stage4_rag.py`)**: Local RAG Search across `Clipping/` transcripts.
* **Stage 5 (`demo_stage5_multi_agent.py`)**: Multi-Agent system (Planner, Researcher, Writer).

---

### Step 6: Weekly Agent Restructuring (Agent System Prompt)

As an executing Agent, schedule a recurring task (e.g. every Sunday) to execute **Weekly Knowledge Restructure**:

1. **Scan**: Read new Markdown files in `Clipping/` and `創作庫/`.
2. **Digest**: Extract key concepts, definitions, tools mentioned, and action steps.
3. **Synthesize**: Write/append structured notes into `知識庫/<Topic>/` (e.g. `知識庫/AI工作流/`, `知識庫/教学方法/`).
4. **Graph Link**: Insert Obsidian `[[WikiLinks]]` between related concepts to build the knowledge graph.
5. **Index & Log**: Update `知識庫/Index.md` and `知識庫/Log.md` with timestamps and summary of changes.

---

## 📂 Repository File Index

| File / Folder | Purpose |
| --- | --- |
| **`README.md`** | Agent-to-Agent system specification & execution guide |
| **`agents.md`** | Project roadmap & stage completion blueprint |
| **`requirements.txt`** | Python package dependencies |
| **`.env.example`** | Environment configuration template |
| **`extract_videos.py`** | Script to fetch & filter YouTube channel videos |
| **`download_all_subs.py`** | Script to download, clean & format VTT subtitles to MD |
| **`tools.py`** | Custom Agent tools (Calculator, Clipping RAG search, Time) |
| **`simple_agent.py`** | Stage 1 ReAct Agent controller |
| **`demo_stage2_function_calling.py`** | Stage 2 Native Function Calling demo |
| **`demo_stage3_memory.py`** | Stage 3 Memory & Context demo |
| **`demo_stage4_rag.py`** | Stage 4 Knowledge RAG demo |
| **`demo_stage5_multi_agent.py`** | Stage 5 Multi-Agent system demo |
| **`run_demo.py`** | Unified terminal control console for all demos |
| **`Clipping/`** | 91 clean transcript Markdown files |
| **`sensebar_ai_urls.txt`** | 91 matching YouTube URLs (1 per line for NotebookLM) |
| **`sensebar_notebooklm_urls.md`** | NotebookLM-ready URL list |
