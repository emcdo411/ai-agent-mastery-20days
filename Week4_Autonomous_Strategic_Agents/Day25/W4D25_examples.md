### ✅ Updated File Instructions

### 1️⃣ Open the file in Notepad

```powershell
notepad "C:\Users\Veteran\ai-agent-mastery-28days\Week4_Autonomous_Strategic_Agents\Day25\W4D25_examples.md"
```

---

### 2️⃣ Paste this **exact template**, then Save & Close

````markdown
# W4D25 — Strategy Modules: Example Outputs

👉 Paste **one example per module**.  
For each:  
1. Show the **raw JSON** exactly as returned (no edits).  
2. Write a **short executive brief** in plain bullets, built directly from the JSON.  

---

## 1) SWOT — Example

**Prompt used:**  
SWOT for {{company}} in {{industry}} ({{geo}}, {{timeframe}}). Use repo context only; cite files.

**Raw JSON (from SWOT)**
```json
{
  "company": "ACME",
  "industry": "AI training",
  "geo": "US",
  "timeframe": "Q4 2025",
  "strengths": [],
  "weaknesses": [],
  "opportunities": [],
  "threats": [],
  "confidence": "Medium",
  "notes": ""
}
```

**Executive Brief**  
- Key strengths: …  
- Weaknesses: …  
- Opportunities: …  
- Threats: …  
**Action Items**  
- …  
**Confidence:** Medium — repo coverage partial  
**Sources:** `Week2_Automation_Workflows/Day9/lesson.md`, `...`

---

## 2) Porter’s Five Forces — Example

**Prompt used:**  
Porter’s for {{company}} / {{industry}} ({{geo}}, {{timeframe}}). Repo citations only.

**Raw JSON (from Porter’s)**
```json
{
  "company": "ACME",
  "industry": "AI training",
  "geo": "US",
  "timeframe": "Q4 2025",
  "forces": [
    { "name": "Threat of New Entrants", "rating": 3, "rationale": "", "sources": [] },
    { "name": "Bargaining Power of Suppliers", "rating": 2, "rationale": "", "sources": [] },
    { "name": "Bargaining Power of Buyers", "rating": 4, "rationale": "", "sources": [] },
    { "name": "Threat of Substitutes", "rating": 3, "rationale": "", "sources": [] },
    { "name": "Industry Rivalry", "rating": 4, "rationale": "", "sources": [] }
  ],
  "overall": { "rating": 3, "comment": "" },
  "confidence": "Medium",
  "notes": ""
}
```

**Executive Brief**  
- New entrants risk: …  
- Supplier power: …  
- Buyer power: …  
- Substitutes threat: …  
- Rivalry intensity: …  
**Action Items**  
- …  
**Confidence:** Medium — repo cites partial  
**Sources:** `...`

---

## 3) OKRs — Example

**Prompt used:**  
Draft OKRs for {{team}} ({{timeframe}}), focus = {{focus}}. Tie KRs to repo metrics.

**Raw JSON (from OKRs)**
```json
{
  "team": "Cohort Ops",
  "timeframe": "H1 2026",
  "objectives": [
    {
      "objective": "Increase completion & placements",
      "key_results": [
        { "kr": "", "metric": "", "baseline": "unknown", "target": "", "source_files": [] },
        { "kr": "", "metric": "", "baseline": "unknown", "target": "", "source_files": [] }
      ],
      "owners": ["Ops Lead"],
      "risks": ["", ""],
      "assumptions": [""]
    }
  ],
  "confidence": "Medium",
  "notes": ""
}
```

**Executive Brief**  
- Objective focus: …  
- Key Results: …  
- Risks & Assumptions: …  
**Action Items**  
- …  
**Confidence:** Medium — repo data limited  
**Sources:** `...`

---

## Notes
- Keep JSON **exactly as returned** (no edits inside code block).  
- Executive briefs = **5–7 bullets** + 3 action items.  
- Always include **Confidence** and **Sources**.  
- Keep the vibe: JSON first, human summary second.  

````

---

### 3️⃣ Commit & Push

```powershell
cd "C:\Users\Veteran\ai-agent-mastery-28days"

git add "Week4_Autonomous_Strategic_Agents/Day25/W4D25_examples.md"
git commit -m "W4D25: add vibe coding examples template (SWOT, Porter, OKRs JSON + briefs)"
git push
```

---





