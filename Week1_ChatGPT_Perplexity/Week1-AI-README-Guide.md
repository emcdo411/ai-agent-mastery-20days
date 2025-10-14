# Week 1 AI Tools Field Guide

*A practical, plain-English reference for the first seven days of your AI Mastery track.*

---

## Table of Contents

* [How to Use This Guide](#how-to-use-this-guide)
* [7-Day Schedule at a Glance](#7-day-schedule-at-a-glance)
* [Quick Decision Guide](#quick-decision-guide)
* [Day-by-Day Playbook](#day-by-day-playbook)

  * [Day 1 — Executive AI Opportunity Workshop](#day-1--executive-ai-opportunity-workshop)
  * [Day 2 — Structured Prompt Engineering (RTF + PICO)](#day-2--structured-prompt-engineering-rtf--pico)
  * [Day 3 — Perplexity → ChatGPT-5 Research Workflow](#day-3--perplexity--chatgpt-5-research-workflow)
  * [Day 4 — Research Agent + Plotly Visualization](#day-4--research-agent--plotly-visualization)
  * [Day 5 — Summarization Agent](#day-5--summarization-agent)
  * [Day 6 — Translation & Localization Agent](#day-6--translation--localization-agent)
  * [Day 7 — Automated Pipeline Agent (Preview)](#day-7--automated-pipeline-agent-preview)
* [Tool Deep Dives](#tool-deep-dives)
* [Prompt Library](#prompt-library)
* [Output Standards & Governance](#output-standards--governance)
* [Evaluation Rubrics & Pitfalls](#evaluation-rubrics--pitfalls)
* [Glossary & File Map](#glossary--file-map)

---

## How to Use This Guide

1. **Scan the 7-Day Schedule** for focus and deliverables.
2. **Pick the Day you’re on** and follow its step checklist.
3. **Copy/paste prompts** from the Playbook or Prompt Library.
4. **Save outputs** using filenames listed in the File Map.
5. **Match your deliverables** to the Output Standards section.

---

## 7-Day Schedule at a Glance

|  Day  | Focus                                 | Primary Tools                     | Key Outputs                                                  |
| :---: | :------------------------------------ | :-------------------------------- | :----------------------------------------------------------- |
| **1** | Executive AI Opportunity Workshop     | ChatGPT-5                         | Use-case canvas + Discovery brief                            |
| **2** | Structured Prompt Engineering         | ChatGPT-5 · Perplexity            | RTF/PICO templates + comparison                              |
| **3** | Research Handoff                      | Perplexity → ChatGPT-5            | Executive summary with sources                               |
| **4** | Research Agent + Plotly Visualization | ChatGPT-5 · Plotly Studio/Express | Dataset + dashboard + research brief                         |
| **5** | Summarization Agent                   | ChatGPT-5                         | Structured executive summary (100/300/600 words)             |
| **6** | Translation & Localization Agent      | ChatGPT-5                         | Bilingual executive brief + localization notes               |
| **7** | Automated Pipeline Agent              | Flowise · Ollama · Chroma         | End-to-end pipeline script + governance report (coming soon) |

---

## Quick Decision Guide

* **Fresh facts or URLs?** → Use **Perplexity AI**.
* **Executive summary or board memo?** → Use **ChatGPT-5 Summarization Agent**.
* **Translation or regional fit?** → Use **Day 6 Localization Agent**.
* **Visualize performance metrics?** → Use **Plotly Express Notebook (Day 4)**.
* **Chain it all together?** → Build the **Automated Pipeline Agent (Day 7)**.

---

## Day-by-Day Playbook

### **Day 1 — Executive AI Opportunity Workshop**

**Goal:** Surface a high-ROI automation use case and scope Phase 1 Paid Discovery.
**Outputs:** Opportunity Canvas + Discovery Brief + Private AI One-Pager.
**File:** `wk01/day01_executive_ai_opportunity_workshop.md`
**Acceptance:** One scored use case, Discovery brief drafted, CRM fields filled.

---

### **Day 2 — Structured Prompt Engineering (RTF + PICO)**

**Goal:** Design reusable prompt templates that yield consistent executive outputs.
**Outputs:** `Day2_structured_prompt.txt`, `Day2_prompt_comparison.md`
**Acceptance:** Structured template tested in both ChatGPT-5 and Perplexity.

---

### **Day 3 — Perplexity → ChatGPT-5 Research Workflow**

**Goal:** Gather fresh, cited facts and turn them into board-ready briefs.
**Outputs:** `Day3_exec_summary.md`, `/logs/day3.md`
**Acceptance:** Fact pack built, conflicts flagged, gaps listed, sources compact.

---

### **Day 4 — Research Agent + Plotly Visualization**

**Goal:** Automate data storytelling with visual and textual outputs.
**Tools:** ChatGPT-5 + Plotly Studio/Express
**Outputs:** `Day4_research_agent_prompt.txt`, `Day4_dataset.csv`, `week1_day4_plotly_express.ipynb`
**Acceptance:** Research brief + dashboard with clean Markdown and saved HTML charts.

---

### **Day 5 — Summarization Agent**

**Goal:** Condense long reports or dashboards into concise executive summaries.
**Outputs:** `Day5_summary_agent.md`, `/logs/day5.md`
**Acceptance:** Word count met, 3 stats cited, tone formal, bilingual option verified.

---

### **Day 6 — Translation & Localization Agent**

**Goal:** Translate and localize executive briefs for target languages and regions.
**Outputs:** `Day6_translation_localization_agent.md`, `/logs/day6.md`
**Acceptance:** Structure mirrored, tone preserved, Localization Notes added.

---

### **Day 7 — Automated Pipeline Agent (Preview)**

**Goal:** Link Days 1–6 into a governed workflow (Research → Summarize → Translate → Visualize).
**Outputs:** `Day7_pipeline_agent.md` (coming soon).
**Acceptance:** All modules triggerable via single prompt chain.

---

## Tool Deep Dives

### **ChatGPT-5 — Analysis & Authoring**

* Long-context reasoning and clean Markdown formatting.
* Ideal for briefs, tables, summaries, translations.
* Pair with Perplexity for live citations.

### **Perplexity AI — Sourced Research**

* Fetches recent data with publisher and URL.
* Use Focus mode for regional queries.
* Validate publisher and date manually.

### **Plotly Studio / Express**

* Create interactive dashboards from structured data.
* Export as HTML and embed in executive reports.

### **Flowise / Ollama / Chroma (Preview)**

* For local-first AI agents and vector memory pipelines (Day 7).

---

## Prompt Library

**RTF Template**

```text
Role: You are a {{country}} {{sector}} advisor for executives.
Task: Identify top 3 opportunities and top 3 risks in {{topic}} for {{year}}.
Format: 150-word brief + Markdown table (Item, Why, Source, Date, Confidence) + 3 next steps.
```

**PICO Template**

```text
Persona: Senior analyst for {{org}} in {{country}}.
Instructions: Use official sources ≤ 24 months; flag gaps; cite publisher + year.
Context: Sector={{sector}}; Topic={{topic}}; Year={{year}}.
Output: Brief ≤150 words, table, limitations, next steps, sources.
```

**Summarization Agent**

```text
1) Executive Summary ({{word_count}} words)
2) 3 Key Stats + Citations
3) 2-Sentence Bilingual Abstract
4) Limitations & Open Questions
5) Sources list
```

**Localization Agent**

```text
Translate and localize this executive summary into {{language}} for {{region}}.
Keep structure and citations; adjust terminology, currency, and tone for executives.
```

---

## Output Standards & Governance

**Markdown Contracts**

* *Executive Brief:* 120–150 words with headings or bullets.
* *Findings Table:* `Theme | Claim | Source | Date | Confidence`.
* *Bilingual Abstract:* Two sentences per language, identical meaning.
* *Sources:* Publisher — Title (Year). URL

**Governance Rules**

* Public data only; no PII/PHI/PCI.
* Cite publisher + year; URLs listed once.
* Version files and log runs (`/logs/dayX.md`).

---

## Evaluation Rubrics & Pitfalls

**Evaluate**

* Structure fidelity
* Readability & tone
* Actionability of next steps
* Source quality & recency
* Consistency across outputs

**Common Fixes**

* Add explicit output schema to prompt.
* Restate word limits and QA rubric inside prompt.
* For broken tables, ask “return as Markdown only.”

---

## Glossary & File Map

| Term           | Meaning                                                |
| :------------- | :----------------------------------------------------- |
| **RTF**        | Role → Task → Format prompt structure.                 |
| **PICO**       | Persona → Instructions → Context → Output.             |
| **Fact Pack**  | Short list of sourced claims from Perplexity.          |
| **Private AI** | Local-first, governed AI posture with no data leakage. |

**Week 1 File Map**

| Day            | File(s)                                                            |
| :------------- | :----------------------------------------------------------------- |
| 1              | `wk01/day01_executive_ai_opportunity_workshop.md`                  |
| 2              | `wk01/day02_structured_prompt_engineering.md`                      |
| 3              | `wk01/day03_perplexity_plus_gpt5_workflow.md`                      |
| 4              | `wk01/day04_research_agent.md` · `week1_day4_plotly_express.ipynb` |
| 5              | `wk01/day05_summarization_agent.md`                                |
| 6              | `wk01/day06_translation_localization_agent.md`                     |
| 7              | `wk01/day07_pipeline_agent.md` (coming soon)                       |
| Toolkit Folder | `/Week1_AI_Toolkit/` → README · prompts · logs · HTML exports      |

---
