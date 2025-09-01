<!-- Licensed under DACR-1.1 — see LICENSE.md -->

# ⚡ Day 9 — Context Engineering for Your AI Pair-Programmer

## 📌 Objective
- Create a **context pack** so Claude/AI tools code to your standards.
- Define **constraints**, **APIs**, and a **system prompt**.

---

## 🛠 Steps (≤30–45 min)

1. **Create folder**
   - `Week2_Vibe_Coding/Day09/context/`

2. **Add files & paste**
   - `README_context.md` — how to use this pack  
   - `constraints.md` — stack, style, security (e.g., “no secrets in code”)  
   - `apis.md` — endpoints with **placeholders** for keys  
   - `glossary.md` — product/domain terms  
   - `system_prompt_coding.md`:
     ```md
     Role: Senior IDE Copilot. Follow repo constraints. Ask before inventing APIs.

     You have:
     - PRD: ../Day08/PRD.md
     - Constraints: ./constraints.md
     - APIs: ./apis.md
     - Glossary: ./glossary.md

     Rules:
     1) Prefer simple, shippable patterns
     2) Generate complete files + minimal tests
     3) If unknown, propose 2 options + tradeoffs
     4) Output diffs or full files, no partials
     ```

3. **Link the pack** in `PRD.md > Links`.

---

## 📂 Deliverables
- Context files above
- `/logs/day9.md` — 3 bullets on decisions
- Commit: `feat(day9): context pack for AI coding`

---

## ✅ Rubric (Self-Check)
- [ ] Constraints are explicit (style, deps, security)
- [ ] APIs documented with placeholders
- [ ] System prompt references PRD/constraints
- [ ] No secret values committed

---

## 📝 Reflection Prompts (Day 9)
1. What does your AI often “hallucinate” without context?
2. Which constraint will prevent future rework?
3. What’s your “single source of truth” file?

---

## 🎯 Role Relevance
- **All disciplines:** Faster, safer AI-assisted coding
- **Leads:** Shared context = consistent outputs

