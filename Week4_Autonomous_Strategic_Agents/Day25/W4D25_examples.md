## W4D25 — Strategy Modules: Example Outputs

### 1️⃣ Open the file in Notepad

```powershell
notepad "C:\Users\Veteran\ai-agent-mastery-28days\Week4_Autonomous_Strategic_Agents\Day25\W4D25_examples.md"
```

---

### 2️⃣ Paste the following **exact template** into Notepad, then **Save** and close

````markdown
# W4D25 — Strategy Modules: Example Outputs

Paste **one example per module**.  
For each: include the **raw JSON** returned by the module, followed by a **short executive brief** generated from that JSON.

---

## 1) SWOT — Example

**Prompt used:**  
SWOT for {{company}} in {{industry}} ({{geo}}, {{timeframe}}). Use repo context only; cite files.

**Raw JSON (from the SWOT module)**
```json
{
  "company": "ACME",
  "industry": "AI training",
  "timeframe": "Q4 2025",
  "strengths": [],
  "weaknesses": [],
  "opportunities": [],
  "threats": [],
  "confidence": "Medium",
  "notes": ""
}
```

**Executive brief (generated from JSON)**  
- …
- …
**Action Items**
- …
**Confidence:** Medium — because …  
**Sources:** `Week2_Automation_Workflows/Day9/lesson.md`, `...`

---

## 2) Porter’s Five Forces — Example

**Prompt used:**  
Porter’s for {{company}} / {{industry}} ({{geo}}, {{timeframe}}). Repo citations only.

**Raw JSON (from the Porter’s module)**
```json
{
  "company": "ACME",
  "industry": "AI training",
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

**Executive brief (generated from JSON)**  
- …
- …
**Action Items**
- …
**Confidence:** Medium — because …  
**Sources:** `...`

---

## 3) OKRs — Example

**Prompt used:**  
Draft OKRs for {{team}} ({{timeframe}}), focus = {{focus}}. Tie KRs to repo metrics.

**Raw JSON (from the OKR module)**
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

**Executive brief (generated from JSON)**  
- …
- …
**Action Items**
- …
**Confidence:** Medium — because …  
**Sources:** `...`

---

## Notes
- Keep JSON **exactly as returned** (no extra prose in the code block).
- Keep briefs to **5–7 bullets** + 3 actions.
- Always include **Confidence** and **Sources**.

````

---

### 3️⃣ Commit & Push

```powershell
cd "C:\Users\Veteran\ai-agent-mastery-28days"

git add "Week4_Autonomous_Strategic_Agents/Day25/W4D25_examples.md"
git commit -m "W4D25: add examples template (JSON + executive brief for SWOT/Porter/OKRs)"
git push
```

💡 *Tip:* Want a **post-processor prompt** for Flowise that turns JSON into an executive brief automatically? Keep this template handy for automation later.

---




