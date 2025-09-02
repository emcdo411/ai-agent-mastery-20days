<!-- Licensed under DACR-1.1 — see LICENSE.md -->

# ⚡ Day 9 — Context Engineering for Your AI Pair-Programmer (Governance + Leadership Lens)

## 📌 Objective
- Build a **context pack** so AI tools (ChatGPT, Claude, Perplexity) operate with your standards.  
- Define **constraints, rules, APIs, and system prompts** that reduce risk and enforce consistency.  
- Extend the practice beyond coding: use context packs for **governance, leadership, and municipal workflows**.  

---

## 🛠 Steps (≤30–45 min)

### 1. **Create folder**
- `Week2_Vibe_Coding/Day09/context/`

### 2. **Add files & paste**
- `README_context.md` — how to use this pack (coding + governance).  
- `constraints.md` — stack, style, **security + governance rules** (e.g., *“no PII in logs,”* *“always cite local sources,”* *“flag bias risk if detected”*).  
- `apis.md` — endpoints with **placeholders** (tech APIs or government datasets).  
- `glossary.md` — product, policy, or municipal terms (e.g., *PRD = project requirements doc*, *MoH = Ministry of Health*).  
- `system_prompt_coding.md`:  
  ```md
  Role: Senior IDE Copilot + Governance Advisor. Follow repo + governance constraints. Ask before inventing APIs.

  You have:
  - PRD: ../Day08/PRD.md
  - Constraints: ./constraints.md
  - APIs: ./apis.md
  - Glossary: ./glossary.md

  Rules:
  1) Prefer simple, shippable, auditable patterns
  2) Generate complete files + minimal tests
  3) If unknown, propose 2 options + tradeoffs
  4) Output diffs or full files, no partials
  5) Apply governance lens: check ethics, compliance, and citizen impact before suggesting
````

### 3. **Link the pack**

* Update `PRD.md > Links` with `../Day09/context/`.

### 4. **Governance Extension**

* Create `system_prompt_governance.md` to guide AI in municipal/leadership scenarios:

  ```md
  Role: Policy Analyst Copilot.  
  Context: Ethiopian municipal office preparing AI-driven citizen services.  
  Rules:  
  - Answer only within policy/governance scope  
  - Always cite government or university sources if available  
  - Flag ethical or bias concerns explicitly  
  - Provide bilingual outputs (English + Amharic placeholder)  
  - Keep tone: professional, government-report ready  
  ```

---

## 📂 Deliverables

* Context files (`README_context.md`, `constraints.md`, `apis.md`, `glossary.md`, `system_prompt_coding.md`, `system_prompt_governance.md`)
* `/logs/day9.md` — 3 bullets on decisions made
* Commit: `feat(day9): context pack for AI coding + governance`

---

## ✅ Rubric (Self-Check)

* [ ] Constraints explicit (style, deps, security, governance)
* [ ] APIs documented with placeholders (tech + civic)
* [ ] System prompt references PRD/constraints
* [ ] Governance prompt included
* [ ] No secret values committed

---

## 📝 Reflection Prompts (Day 9)

1. What does your AI often “hallucinate” without context?
2. Which constraint (tech or governance) will prevent the most future rework?
3. What’s your “single source of truth” file — PRD, glossary, or checklist?
4. How could a **governance context pack** keep municipal projects aligned with law + ethics?

---

## 🎯 Role Relevance

* **All Disciplines:** Faster, safer AI-assisted coding + governance workflows.
* **Leads/PMs:** Shared context = consistent outputs across teams.
* **Policy/Government:** Context packs ensure AI agents respect **local laws, ethics, and citizen trust**.
* **Municipal Leaders (Ethiopia/Caribbean):** Use governance packs as “guardrails” for citizen-facing AI services.

```

---

✨ This way, **Day 9 bridges coding → governance**, showing learners how the same **context engineering discipline** works for both software *and* political/municipal workflows.  

