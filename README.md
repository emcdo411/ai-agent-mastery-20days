# 🚀 AI Agent Mastery: 20-Day Professional Track

[![License: DACR](https://img.shields.io/badge/license-DACR-blue?style=for-the-badge)](LICENSE)
[![AI Tools](https://img.shields.io/badge/AI-Tools-green?style=for-the-badge\&logo=openai)]()
[![Professional Track](https://img.shields.io/badge/Professional%20Track-Yes-orange?style=for-the-badge)]()
[![GitHub Repo Size](https://img.shields.io/github/repo-size/emcdo411/ai-agent-mastery-28days?style=for-the-badge\&color=purple)]()

---

## 📑 Table of Contents

* [Overview](#overview)
* [Who This Is For](#who-this-is-for)
* [Learning Outcomes](#learning-outcomes)
* [Professional Deliverables](#professional-deliverables)
* [Course Structure](#course-structure)
* [Folder Structure](#folder-structure)
* [Week 1: Foundations (Days 1–5)](#week-1-foundations-days-1–5)
* [Week 2: Governance & Workflows (Days 6–10)](#week-2-governance--workflows-days-6–10)
* [Week 3: Data Agents (Days 11–15)](#week-3-data-agents-days-11–15)
* [Week 4: Strategic Agents (Days 16–20)](#week-4-strategic-agents-days-16–20)
* [Mermaid Workflow Diagram](#mermaid-workflow-diagram)
* [License](#license)

---

## Overview

The **AI Agent Mastery: 20-Day Professional Track** is a *career-focused builder program* for professionals, analysts, and leaders who want to design **deployable, boardroom-ready AI agents** in under an hour.

It’s optimized for **local-first tools (Ollama, Chroma, Flowise, FastAPI)** with **Ethiopia-relevant use cases** (healthcare, permits, budgeting, policy simulations).

No fluff.
No “someday” theory.
Every day ends with an artifact you can commit, demo, or present.

---

## Who This Is For

* **Data & Policy Professionals:** Build auditable AI workflows with citations.
* **Entrepreneurs & Nonprofits:** Prototype civic and financial micro-tools.
* **Analysts & MBAs:** Apply frameworks (SWOT, Porter’s, OKRs) with repo evidence.
* **Military Transitioners:** Convert mission planning into AI simulations.
* **Public-Sector Leaders:** Use local-first AI to stress-test policies before rollout.

---

## Learning Outcomes

By the end, you can:

* Deploy **repo-grounded RAG agents** with Flowise + Ollama.
* Use **retrievers, routers, and guardrails** for safe outputs.
* Build **scenario planners** (Monte Carlo-lite) and brief clearly.
* Apply **strategic frameworks** (SWOT, Porter, OKRs) with JSON → briefs.
* Run **boardroom demos** with citations, probabilities, and one-click scripts.

---

## Professional Deliverables

You’ll graduate with:

* 📄 **Strategic Prompt Files** (SWOT, Porter’s, OKRs, Exec Brief)
* 📊 **Flowise Chatflows** (file search, CSV summary, RAG, scenario runner)
* 🤖 **Autonomous agent** with memory + refreshable RAG
* 🎥 **Stakeholder demo pack** (screenshots, scripts, reports)
* 📑 **Ethiopia-focused case study** mapping problem → solution → KPIs

---

## Course Structure

* **Week 1 (Days 1–5):** Prompt discipline, repo grounding, research → first Q\&A bot.
* **Week 2 (Days 6–10):** Governance flows, context packs, SDLC gates, Git, deploy.
* **Week 3 (Days 11–15):** Data agents, visualization briefs, ranking/trend outputs.
* **Week 4 (Days 16–20):** Local RAG (Day16), multi-tool agent (Day17), refreshable memory (Day18), strategy modules (Day19), scenario planner + final assets/demo (Day20).

Each week ends with a **rubric check**: ✅ Runs | ✅ Documented | ✅ Deployed | ✅ Cited | ✅ KPI-ready.

---

## Folder Structure

```plaintext
ai-agent-mastery-28days/
│
├── Week1_Foundations/
│   ├── Day1/ ...
│   ├── Day5/ ...
│
├── Week2_Governance_Workflows/
│   ├── Day6/  ...
│   ├── Day10/ ...
│
├── Week3_Data_Agents/
│   ├── Day11/ ...
│   ├── Day15/ ...
│
├── Week4_Autonomous_Strategic_Agents/
│   ├── Day16/  # Local RAG (Flowise + Ollama + Chroma)
│   ├── Day17/  # Multi-Tool agent (File Search + CSV + RAG)
│   ├── Day18/  # Refreshable RAG (memory refresh, citations, guardrails)
│   ├── Day19/  # Strategy modules (SWOT, Porter’s, OKRs + exec brief)
│   ├── Day20/  # Scenario planner + final assets/investor demo
│
├── scripts/        # FastAPI server (local_tools_server.py)
├── assets/         # Evidence pack (screenshots, charts, exports)
├── templates/      # Strategic prompts (SWOT, Porter, OKRs, Exec Brief)
├── docs/           # Diagrams, case studies, rubrics
└── README.md
```

---

## Week 1: Foundations (Days 1–5)

* Prompting, repo-grounded research, synthesis, first domain-limited Q\&A bot.
* **Deliverable:** Foundations agent (clean Markdown, citations, optional bilingual line).

---

## Week 2: Governance & Workflows (Days 6–10)

* Political strategy flows, context packs, SDLC with governance gates, Git PRs, deploy a simple site/app.
* **Deliverables:** Governance prompts, PRD v2, demo script, basic live link.

---

## Week 3: Data Agents (Days 11–15)

* Analysis + visualization briefs, ranking/trend charts, tidy CSVs, dataset summaries.
* **Deliverables:** Charts, “insights.md”, and a small data-agent brief.

---

## Week 4: Strategic Agents (Days 16–20)

* **Day 16:** Local RAG agent (Flowise + Ollama + Chroma) with filename citations.
* **Day 17:** Multi-tool agent (File Search + CSV Summary + RAG fallback via router).
* **Day 18:** Refreshable RAG (type “refresh memory”), guardrails, confidence & sources.
* **Day 19:** Strategy modules — **SWOT, Porter’s, OKRs** (JSON-only prompts + exec brief).
* **Day 20:** Scenario planner (Monte Carlo-lite) **+ final assets & investor demo pack**.
* **Deliverables:** Agent chatflows, strategy prompts, scenario report, final “assets” package.

---

## Mermaid Workflow Diagram

```mermaid
flowchart TD
  IN[Chat Input] --> ROUTE{Route intent}

  ROUTE -->|simulate| SIM_BUILD[Build scenario JSON]
  SIM_BUILD --> SIM_HTTP[HTTP POST scenario run]
  SIM_HTTP --> SIM_SUM[Summarize to brief]
  SIM_SUM --> OUT_SIM[Output (simulation)]

  ROUTE -->|find / where / file| FS_HTTP[HTTP GET file search]
  FS_HTTP --> FS_SUM[Summarize matches (≤10)]
  FS_SUM --> OUT_FIND[Output (file search)]

  ROUTE -->|csv / columns / summary| CSV_HTTP[HTTP POST CSV summary]
  CSV_HTTP --> CSV_SUM[Profile rows/cols/nulls]
  CSV_SUM --> OUT_CSV[Output (CSV summary)]

  ROUTE -->|refresh memory| LOAD[Load local docs]
  LOAD --> SPLIT[Split 1000/150]
  SPLIT --> EMB[Embeddings (Ollama)]
  EMB --> UP[Chroma Upsert]
  UP --> OUT_REFRESH[Output (memory refreshed)]

  ROUTE -->|else| RETR[Retriever (Chroma)]
  RETR --> P_GUARD[Prompt (guardrails + citations)]
  P_GUARD --> LLM[Ollama LLM]
  LLM --> FORMAT[Bullets + Actions + Confidence + Sources]
  FORMAT --> OUT_RAG[Output (RAG)]
```

---

## License

This project is licensed under the **DACR License** — see the [LICENSE](LICENSE) file for details.





