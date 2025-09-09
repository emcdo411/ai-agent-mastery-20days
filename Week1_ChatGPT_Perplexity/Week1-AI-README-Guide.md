# Week 1 AI Tools Field Guide

> A plain‑English guide to the tools and workflows you’ll use in a 5‑day Week 1. It balances clarity for non‑technical learners with enough depth for technical readers.

---

## Table of Contents

* [How to Use This Guide](#how-to-use-this-guide)
* [5‑Day Schedule at a Glance](#5-day-schedule-at-a-glance)
* [Quick Decision Guide](#quick-decision-guide)
* [Day‑by‑Day Playbook](#day-by-day-playbook)

  * [Day 1 — Setup, Safety, and Tool Comparison](#day-1--setup-safety-and-tool-comparison)
  * [Day 2 — Structured Prompting (RTF + PICO)](#day-2--structured-prompting-rtf--pico)
  * [Day 3 — Research Handoff (Perplexity → ChatGPT‑5)](#day-3--research-handoff-perplexity--chatgpt5)
  * [Day 4 — Research & Summarization Agents](#day-4--research--summarization-agents)
  * [Day 5 — Domain Q\&A Bot + Toolkit Packaging](#day-5--domain-qa-bot--toolkit-packaging)
* [Tool Deep Dives (Reference)](#tool-deep-dives-reference)

  * [ChatGPT‑5 (Analysis & Writing)](#chatgpt5-analysis--writing)
  * [Perplexity AI (Sourced Research)](#perplexity-ai-sourced-research)
  * [Structured Prompting: RTF & PICO](#structured-prompting-rtf--pico)
  * [Handoff Workflow](#handoff-workflow)
  * [Research Agent](#research-agent)
  * [Summarization Agent](#summarization-agent)
  * [Domain‑Specific Q\&A Bot](#domain-specific-qa-bot)
  * [Week 1 AI Toolkit](#week-1-ai-toolkit)
* [If You’re Non‑Technical: Start Here](#if-youre-non-technical-start-here)
* [If You’re Technical: Options & Integrations](#if-youre-technical-options--integrations)
* [Prompt Library: Starter Snippets](#prompt-library-starter-snippets)
* [Output Standards: Markdown Contracts](#output-standards-markdown-contracts)
* [Governance & Safety (Private AI)](#governance--safety-private-ai)
* [Evaluation & Rubrics](#evaluation--rubrics)
* [Common Pitfalls & Fixes](#common-pitfalls--fixes)
* [Glossary](#glossary)
* [Appendix: File Map (5‑Day Track)](#appendix-file-map-5-day-track)

---

## How to Use This Guide

1. **Skim the 5‑day schedule** to see what happens each day.
2. Use the **Quick Decision Guide** to choose a tool in under a minute.
3. Jump into the **Day‑by‑Day Playbook** for steps, prompts, and acceptance criteria.
4. Copy/prompts from the **Prompt Library** and adapt them (country, sector, topic, year).
5. Match outputs to the **Output Standards** so everything you ship looks professional.

---

## 5‑Day Schedule at a Glance

| Day   | Focus                                       | Primary Tools                               | Outputs                               |
| ----- | ------------------------------------------- | ------------------------------------------- | ------------------------------------- |
| **1** | Setup, safety, side‑by‑side tool comparison | ChatGPT‑5, Perplexity                       | Comparison file + reflection          |
| **2** | Structured prompting for consistency        | RTF, PICO, ChatGPT‑5, Perplexity            | Reusable prompt template + comparison |
| **3** | Research handoff workflow                   | Perplexity → ChatGPT‑5                      | Executive summary with sources        |
| **4** | Reusable agents                             | Research Agent, Summarization Agent (GPT‑5) | Research brief + fixed‑length summary |
| **5** | Domain Q\&A + packaging                     | Domain Bot (GPT‑5), Week 1 Toolkit          | Domain transcript + packaged toolkit  |

> **Note:** In the original 7‑day plan, “Domain Bot” (Day 6) and “Toolkit” (Day 7) are now combined into **Day 5**.

---

## Quick Decision Guide

* **Need citations or fresh links?** → Start with **Perplexity**.
* **Need a clean, executive brief now?** → Use **ChatGPT‑5** with **Research Agent** or **Summarization Agent**.
* **Want consistent results across countries/topics?** → Use **RTF/PICO templates**.
* **Need a scope‑bound FAQ/assistant?** → Build the **Domain Q\&A Bot** (Day 5).
* **Presenting work to a stakeholder?** → Package deliverables in the **Week 1 Toolkit** (Day 5).

---

## Day‑by‑Day Playbook

### Day 1 — Setup, Safety, and Tool Comparison

**Goal:** Create accounts, learn safe usage, and compare **ChatGPT‑5** vs **Perplexity** on a local query.

* **Do this:**

  1. Create accounts; review `data_safety_checklist.md`.
  2. Run the **same country‑specific prompt** in both tools.
  3. Save results and write a brief reflection.
* **Deliverables:** `Day1_comparison.md`, `/logs/day1.md`
* **Acceptance:** Country‑specific prompt; both outputs captured; reflection complete.

### Day 2 — Structured Prompting (RTF + PICO)

**Goal:** Standardize how you ask for work to get repeatable, clean outputs.

* **Do this:**

  1. Draft an **RTF** and a **PICO** template with placeholders.
  2. Run in **ChatGPT‑5**; cross‑check with **Perplexity** when sources matter.
* **Deliverables:** `Day2_structured_prompt.txt`, `Day2_prompt_comparison.md`, `/logs/day2.md`
* **Acceptance:** Output matches the contract (sections, tables, limits).

### Day 3 — Research Handoff (Perplexity → ChatGPT‑5)

**Goal:** Combine Perplexity’s sourced facts with GPT‑5’s analysis.

* **Do this:**

  1. Build a **fact pack** (title, publisher, URL, date, claim).
  2. Use the **handoff prompt** to produce an executive brief.
* **Deliverables:** `Day3_exec_summary.md`, `/logs/day3.md`
* **Acceptance:** Conflicts flagged; gaps listed; compact citations + Sources section.

### Day 4 — Research & Summarization Agents

**Goal:** Productize repeatable outputs.

* **Do this:**

  1. Run **Research Agent** (brief + findings table + gaps + steps).
  2. Run **Summarization Agent** at 100/300/600 words on a report.
* **Deliverables:** `Day4_research_test_output.md`, `Day5_summary_agent.md` (yes, created on Day 4 in this 5‑day cadence), `/logs/day4.md`
* **Acceptance:** Clean Markdown, word limits obeyed, citations present.

### Day 5 — Domain Q\&A Bot + Toolkit Packaging

**Goal:** Ship a scope‑bound advisor and package your week’s work.

* **Do this:**

  1. Build **Domain Bot** with scope lists + refusal templates.
  2. Test in‑scope and off‑scope questions; export transcript.
  3. Package prompts/outputs/logs into `/Week1_AI_Toolkit` with a README and versioned filenames.
* **Deliverables:** `Day6_domain_bot.md` (treated as Day 5 artifact), `/Week1_AI_Toolkit/…`, `/logs/day5.md`
* **Acceptance:** Polite refusals; ≤200‑word answers; toolkit README with inventory table.

---

## Tool Deep Dives (Reference)

### ChatGPT‑5 (Analysis & Writing)

**What it does:** Turns prompts and context into structured outputs: briefs, tables, checklists, bilingual summaries.

**When to use:** To convert research into decision‑ready deliverables.

**Inputs:** Task + context (country, sector, topic, year).
**Outputs:** Markdown briefs, tables, action plans, translations.

**Strengths:** Strong formatting, longer context handling, better multi‑step reasoning.
**Limits:** Doesn’t fetch URLs; pair with Perplexity for citations.

---

### Perplexity AI (Sourced Research)

**What it does:** Finds recent information with links and dates.

**When to use:** When you need citations or to validate facts quickly.

**Inputs:** Localized question; Focus mode.
**Outputs:** Sourced responses with URLs/dates.

**Strengths:** Fast, sourced.
**Limits:** Source quality varies; always check publisher + date.

---

### Structured Prompting: RTF & PICO

**RTF:** Role → Task → Format (fast).
**PICO:** Persona → Instructions → Context → Output (repeatable).

**Use:** Keep output schema stable; change only the context.

---

### Handoff Workflow

**Use:** Perplexity for facts → ChatGPT‑5 for analysis/formatting.
**Output:** Executive summary + findings table + gaps + next steps + sources.

---

### Research Agent

**Use:** Topic‑agnostic research briefs across countries/sectors.
**Output:** 120–150‑word brief + findings table + gaps + next steps + sources.

---

### Summarization Agent

**Use:** Condense 2–3 page reports at 100/300/600 words.
**Output:** Structured summary + 3 stats + optional bilingual abstract.

---

### Domain‑Specific Q\&A Bot

**Use:** Scope‑bound answers; polite refusals off‑scope.
**Output:** Concise replies (≤200 words) or refusal + compact citations.

---

### Week 1 AI Toolkit

**Use:** Package prompts/outputs/logs into a versioned folder with README.
**Output:** `/Week1_AI_Toolkit` ready for stakeholders.

---

## If You’re Non‑Technical: Start Here

1. Start with the **Summarization Agent** to condense a report you already have.
2. Use **RTF** with ChatGPT‑5 to create a short local brief.
3. When you need sources, run **Perplexity** and paste a fact pack into **ChatGPT‑5**.
4. Save everything using the filenames shown in each day’s lesson.

You don’t need code—just the templates in this guide.

---

## If You’re Technical: Options & Integrations

* **Versioning:** Use SemVer in filenames (e.g., `_v1.0.1`).
* **Automation:** Script copying outputs into `/Week1_AI_Toolkit`.
* **Validation:** Add a linter that checks for required sections.
* **Data posture:** Keep **Private AI** standards (no sensitive data).

---

## Prompt Library: Starter Snippets

**RTF (general):**

```
Role: You are a {{country}} {{sector}} advisor writing for executives.
Task: Identify top 3 opportunities and top 3 risks in {{topic}} for {{year}} with recent public sources.
Format: Executive brief (120–150 words) + Markdown table (Item, Why it matters, Source, Date, Confidence) + 3 next steps.
```

**PICO (repeatable):**

```
Persona: Senior analyst for {{org}} in {{country}}.
Instructions: Use government/university/multilateral sources ≤ 24 months; show gaps; cite publisher + year.
Context: Sector={{sector}}; Topic={{topic}}; Year={{year}}.
Output: Brief (≤150 words), findings table, limitations, next steps, sources.
```

**Handoff (Perplexity → GPT‑5):**

```
Input: I will paste a fact pack (title, publisher, URL, date, claim).
Task: Deduplicate, note conflicts, and produce an executive summary + findings table + gaps + next steps + sources.
```

**Domain Refusal (Day 5):**

```
That is outside this assistant’s domain. Please ask about {{domain}} topics such as {{topics_list}}.
```

---

## Output Standards: Markdown Contracts

* **Executive Brief:** 120–150 words; 3–5 bullets or one short paragraph.
* **Findings Table:** `Theme | Claim | Source | Date | Confidence`.
* **Sources:** Publisher — Title (Year). URL
* **Bilingual Abstract:** Two sentences per language, mirror meaning.

Keeping these contracts stable makes your outputs consistent and easy to scan.

---

## Governance & Safety (Private AI)

* **Public data only** in prompts and uploads.
* **No shared secrets**; prefer OAuth/OIDC scopes (if/when you integrate).
* **Citations** include publisher and year; list URLs once in a Sources section.
* **Evidence** of process: keep logs (`/logs/dayX.md`) and versioned files.

---

## Evaluation & Rubrics

* **Structure fidelity** (sections present, tables complete).
* **Readability** (exec tone, plain English).
* **Actionability** (clear next steps).
* **Source quality** (credible publishers, recent dates).
* **Consistency** (similar outputs across topics/countries).

---

## Common Pitfalls & Fixes

* **Vague prompts → vague outputs:** Use RTF or PICO and specify outputs.
* **Broken formatting:** Ask for **Markdown** and list required sections.
* **No sources:** Start with **Perplexity**; add publisher + year to each claim.
* **Scope drift in Q\&A:** Tighten the out‑of‑scope list and shorten max answer length.

---

## Glossary

* **RTF:** Role → Task → Format.
* **PICO:** Persona → Instructions → Context → Output.
* **Fact pack:** Short, sourced notes you pass from Perplexity to ChatGPT‑5.
* **Private AI:** Operating posture that keeps your data private and governed.

---

## Appendix: File Map (5‑Day Track)

**Recommended mapping** (re‑use existing files where applicable):

* **Day 1:** `wk01/day01_executive_ai_opportunity_workshop.md`
* **Day 2:** `wk01/day02_structured_prompt_engineering.md`
* **Day 3:** `wk01/day03_perplexity_plus_gpt5_workflow.md`
* **Day 4:** `wk01/day04_research_agent.md`, `wk01/day05_summarization_agent.md`
* **Day 5:** `wk01/day06_domain_specific_qa_bot.md` (Domain Bot transcript), `wk01/day07_toolkit_review_and_deployment.md` (Toolkit packaging)

**Packaged folder created on Day 5:**

* `/Week1_AI_Toolkit/` → README, prompts, outputs, logs, templates.

---

\*\*You now have a 5‑day path to consistent, executive‑ready outputs—plus a packaging standard so stakeholders can review your wo
