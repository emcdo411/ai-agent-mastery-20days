# ⚡ Day 7 — Context Engineering & the Automated Pipeline Agent

*(Governance + Leadership Lens)*

## 🎯 Purpose

Turn everything from Days 1–6 into a **repeatable, governed workflow**.
You’ll build a **Context Pack** (constraints + rules + APIs + glossary + system prompts) and a minimal **Pipeline Agent** spec that chains:
**Research → Summarize → Localize → Visualize → Package** — with governance guardrails.

---

## 📌 Objectives

* Design a reusable **Context Pack** so ChatGPT/Claude/Perplexity operate with your standards.
* Define **constraints, rules, API placeholders, and system prompts** for both coding and governance use.
* Create a **lightweight pipeline spec** that sequences the Day 3–6 steps with inputs/outputs.
* Ship artifacts that are easy for leaders to audit and for engineers to extend.

---

## 🛠 Agenda (30–45 min)

|  Time | Task                                      |
| :---: | :---------------------------------------- |
|  0–10 | Create folders; paste Context Pack files  |
| 10–25 | Add system prompts (coding + governance)  |
| 25–40 | Write the Pipeline Agent spec (JSON/YAML) |
| 40–45 | Save, reflect, and commit                 |

---

## 📁 Folders (Week 1)

Create:

```
wk01/day07/
wk01/day07/context/
wk01/day07/pipeline/
```

---

## 📄 Files to Add (paste the templates below)

### 1) `wk01/day07/context/README_context.md`

```md
# Context Pack (Coding + Governance)

Purpose: give AI tools (ChatGPT/Claude/Perplexity) a shared context and ruleset so outputs are
consistent, safe, and aligned with your repo standards and governance posture.

Contents:
- constraints.md — language, style, security, governance rules
- apis.md — endpoints (placeholders), required headers/scopes, example calls
- glossary.md — product/policy terms and abbreviations
- system_prompt_coding.md — IDE Copilot + Governance Advisor
- system_prompt_governance.md — Policy Analyst Copilot for leadership/municipal use

How to use:
1) Paste the relevant system prompt into your AI tool.
2) Attach constraints.md, apis.md, and glossary.md as context (or paste sections).
3) For tasks that involve data or policy, ask for an “Evidence & Risks” box at the end.
4) Keep this pack versioned; update constraints when governance changes.
```

### 2) `wk01/day07/context/constraints.md`

```md
# Constraints (Tech + Governance)

## Tech & Style
- Language: Python 3.11; Node optional for tooling.
- Tests: Pytest minimal; prefer pure functions and small modules.
- Structure: production-ready files; include README or docstring.
- Output: full files or diffs; avoid partial fragments.

## Security & Privacy
- No secrets in code or logs. Use env vars / secret stores.
- No PII/PHI/PCI in prompts, outputs, or telemetry.
- Use OAuth2/OIDC scopes for any API (no shared credentials).
- Encrypt at rest/in transit when applicable.

## Governance & Evidence
- Cite publisher + year for external claims; list URLs once in “Sources.”
- For policy/government tasks: show Limitations + Risks; note jurisdiction.
- Add “Decision Impact” bullets for executive/board packets.
- Prefer local-first options; if cloud is used, document data boundary.

## UX/Comms
- Executive tone; skimmable headings; <= 300-word summaries unless specified.
- Bilingual sections must mirror structure exactly.

## Change Control
- Version files with SemVer in filenames when helpful.
- Include a one-line “Decision Log” in commits for governance tasks.
```

### 3) `wk01/day07/context/apis.md`

```md
# APIs (Placeholders)

## Plotly Export (example)
- Endpoint: POST https://api.internal.example/plot/export
- Auth: Bearer {{TOKEN}}
- Body: { "chart_id": "{{id}}", "format": "png|pdf|html" }

## Document Store
- Endpoint: PUT s3://{{bucket}}/reports/{{date}}/exec_summary.md
- Auth: IAM role / OIDC
- Notes: server-side encryption enabled; no PII

## Public Data (Civic)
- Source: {{country}} open data portal
- Access: HTTPS GET with pagination
- Constraint: respect rate limits; cache by day
```

### 4) `wk01/day07/context/glossary.md`

```md
# Glossary (Product + Policy)
- PRD — Product Requirements Document
- FCR — Feed Conversion Ratio (lower is better)
- ADG — Average Daily Gain
- SoR/SoT — System of Record / System of Truth
- CAB — Change Advisory Board (here: “CAB-as-code” pattern)
- Private AI — AI posture that keeps data governed and tenant-bound
```

### 5) `wk01/day07/context/system_prompt_coding.md`

```md
Role: Senior IDE Copilot + Governance Advisor. Follow repo + governance constraints. Ask before inventing APIs.

You have:
- PRD: ../(if available)/PRD.md
- Constraints: ./constraints.md
- APIs: ./apis.md
- Glossary: ./glossary.md

Rules:
1) Prefer simple, shippable, auditable patterns.
2) Generate complete files + minimal tests.
3) If unknown, propose 2 options + tradeoffs.
4) Output diffs or full files, no partials.
5) Apply governance lens: check ethics, compliance, and citizen impact before suggesting.

Return:
- The file(s) or diff(s).
- A short “Evidence & Risks” box (bullets).
- A one-line “Decision Log” message.
```

### 6) `wk01/day07/context/system_prompt_governance.md`

```md
Role: Policy Analyst Copilot.

Context: Municipal or enterprise program office preparing AI-driven services.
Use the context pack; respect constraints.md (privacy, security, governance).

Rules:
- Stay within policy/governance scope.
- Cite government/university sources when available (Publisher, Year); list URLs once.
- Flag ethical/bias concerns and data gaps explicitly.
- Provide bilingual outputs (English + {{local language placeholder}}) when asked.
- Tone: professional, government-report ready.

Return:
- Executive brief with headings.
- Findings table with compact citations.
- “Limitations & Risks” section.
- “Recommended Next Steps” (3 bullets).
```

---

## 🤖 Pipeline Agent (Minimal Spec)

### 7) `wk01/day07/pipeline/pipeline.json`

```json
{
  "name": "week1_pipeline_agent",
  "version": "1.0.0",
  "steps": [
    {
      "id": "research",
      "tool": "perplexity",
      "input": "Day3_factpack.txt",
      "output": "Day3_exec_summary.md",
      "notes": "Gather cited facts; compact publisher/year."
    },
    {
      "id": "summarize",
      "tool": "chatgpt5",
      "input": "Day4_exec_narrative.md",
      "params": { "word_count": 300, "bilingual": false },
      "output": "Day5_summary_agent.md",
      "notes": "Use Day 5 template; add 3 stats."
    },
    {
      "id": "localize",
      "tool": "chatgpt5",
      "input": "Day5_summary_agent.md",
      "params": { "target_language": "Spanish", "region": "MX" },
      "output": "Day6_translation_localization_agent.md",
      "notes": "Preserve structure; add Localization Notes."
    },
    {
      "id": "visualize",
      "tool": "plotly",
      "input": "Day4_dataset.csv",
      "output": "week1/exports/*.html",
      "notes": "KPIs + FCR/ADG/ROI charts; saved HTMLs."
    },
    {
      "id": "package",
      "tool": "packager",
      "inputs": [
        "Day5_summary_agent.md",
        "Day6_translation_localization_agent.md",
        "week1/exports/"
      ],
      "output": "Week1_AI_Toolkit/",
      "notes": "Toolkit README + inventory table."
    }
  ],
  "governance": {
    "constraints": "wk01/day07/context/constraints.md",
    "evidence_required": true,
    "log_path": "logs/day7.md"
  }
}
```

### 8) `wk01/day07/pipeline/README_pipeline.md`

```md
# Week 1 Pipeline Agent

This minimal spec chains the Week 1 artifacts:
Perplexity → ChatGPT-5 (Summarize) → ChatGPT-5 (Localize) → Plotly (Visualize) → Package.

How to run (manual mode):
1) Ensure Day 3–6 deliverables exist.
2) Execute each step using the specified tool and inputs/outputs.
3) Save exported charts to `week1/exports/` and then copy all to `/Week1_AI_Toolkit/`.

Governance notes:
- Keep compact citations (Publisher, Year) and URLs in a Sources section.
- Add a “Limitations & Risks” box to summaries and governance docs.
- Update `logs/day7.md` with a one-line Decision Log for each step.
```

---

## 🧪 Acceptance (Definition of Done)

* **Context Pack** present with constraints, APIs, glossary, and two system prompts.
* **Pipeline spec** written (JSON) with clear inputs/outputs for Steps 1–5.
* **Governance hooks**: Evidence & Risks, compact citations, Decision Log line.
* **No secrets** in any committed file.

---

## 📂 Deliverables

* `wk01/day07/context/*` (all five files)
* `wk01/day07/pipeline/pipeline.json` & `README_pipeline.md`
* `/logs/day7.md` — 3 bullets on key decisions
* Commit: `feat(day7): context pack + week1 pipeline agent`

---

## 📝 Reflection Prompts (Day 7)

1. Without the context pack, what does your AI **hallucinate** or forget most often?
2. Which **constraint** will prevent the most rework or risk?
3. What’s your **single source of truth** (PRD, glossary, or checklist) and why?
4. How could a **governance context pack** keep municipal projects aligned with law and ethics?

---

## 🧭 Workflow (Mermaid)

```mermaid
flowchart TB
  subgraph Context_Pack
    C1[constraints.md]
    C2[apis.md]
    C3[glossary.md]
    C4[system_prompt_coding.md]
    C5[system_prompt_governance.md]
  end

  A[Start] --> B[Create folders]
  B --> C[Add Context Pack files]
  C --> D[Author Pipeline Spec (pipeline.json)]
  D --> E[Run steps Research→Summarize→Localize→Visualize→Package]
  E --> F[Save exports to Week1_AI_Toolkit]
  F --> G[Log decisions in logs/day7.md]
  G --> H[Done]

  Context_Pack --- D
```

---

## 💡 Tips

* Keep **labels ASCII-only** in Mermaid if GitHub parsing ever fails.
* When you paste system prompts into ChatGPT, include a one-line **Task** and ask for **Evidence & Risks** at the end.
* For handoffs, keep filenames and sections **predictable** so later steps don’t drift.
* If you add automation later (Flowise/Ollama/Chroma), start by mirroring this **pipeline.json**.

---
