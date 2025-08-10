\### 1) Open the file in Notepad



```powershell

notepad "C:\\Users\\Veteran\\ai-agent-mastery-28days\\Week4\_Autonomous\_Strategic\_Agents\\Day25\\W4D25\_examples.md"

```



\### 2) Paste this EXACT content into Notepad, then \*\*Save\*\* and close



````

\# W4D25 — Strategy Modules: Example Outputs



Paste ONE example per module: the raw JSON from the module, then a short executive brief your agent produced from that JSON.



---



\## 1) SWOT — Example

\*\*Prompt used:\*\*  

SWOT for {{company}} in {{industry}} ({{geo}}, {{timeframe}}). Use repo context only; cite files.



\*\*Raw JSON (from the SWOT module)\*\*

```json

{

&nbsp; "company": "ACME",

&nbsp; "industry": "AI training",

&nbsp; "timeframe": "Q4 2025",

&nbsp; "strengths": \[],

&nbsp; "weaknesses": \[],

&nbsp; "opportunities": \[],

&nbsp; "threats": \[],

&nbsp; "confidence": "Medium",

&nbsp; "notes": ""

}

````



\*\*Executive brief (generated from JSON)\*\*



\* …

\* …

&nbsp; \*\*Action Items\*\*

\* …

&nbsp; \*\*Confidence:\*\* Medium — because …

&nbsp; \*\*Sources:\*\* `Week2\_Automation\_Workflows/Day9/lesson.md`, `...`



---



\## 2) Porter’s Five Forces — Example



\*\*Prompt used:\*\*

Porter’s for {{company}} / {{industry}} ({{geo}}, {{timeframe}}). Repo citations only.



\*\*Raw JSON (from the Porter’s module)\*\*



```json

{

&nbsp; "company": "ACME",

&nbsp; "industry": "AI training",

&nbsp; "timeframe": "Q4 2025",

&nbsp; "forces": \[

&nbsp;   { "name": "Threat of New Entrants", "rating": 3, "rationale": "", "sources": \[] },

&nbsp;   { "name": "Bargaining Power of Suppliers", "rating": 2, "rationale": "", "sources": \[] },

&nbsp;   { "name": "Bargaining Power of Buyers", "rating": 4, "rationale": "", "sources": \[] },

&nbsp;   { "name": "Threat of Substitutes", "rating": 3, "rationale": "", "sources": \[] },

&nbsp;   { "name": "Industry Rivalry", "rating": 4, "rationale": "", "sources": \[] }

&nbsp; ],

&nbsp; "overall": { "rating": 3, "comment": "" },

&nbsp; "confidence": "Medium",

&nbsp; "notes": ""

}

```



\*\*Executive brief (generated from JSON)\*\*



\* …

\* …

&nbsp; \*\*Action Items\*\*

\* …

&nbsp; \*\*Confidence:\*\* Medium — because …

&nbsp; \*\*Sources:\*\* `...`



---



\## 3) OKRs — Example



\*\*Prompt used:\*\*

Draft OKRs for {{team}} ({{timeframe}}), focus = {{focus}}. Tie KRs to repo metrics.



\*\*Raw JSON (from the OKR module)\*\*



```json

{

&nbsp; "team": "Cohort Ops",

&nbsp; "timeframe": "H1 2026",

&nbsp; "objectives": \[

&nbsp;   {

&nbsp;     "objective": "Increase completion \& placements",

&nbsp;     "key\_results": \[

&nbsp;       { "kr": "", "metric": "", "baseline": "unknown", "target": "", "source\_files": \[] },

&nbsp;       { "kr": "", "metric": "", "baseline": "unknown", "target": "", "source\_files": \[] }

&nbsp;     ],

&nbsp;     "owners": \["Ops Lead"],

&nbsp;     "risks": \["", ""],

&nbsp;     "assumptions": \[""]

&nbsp;   }

&nbsp; ],

&nbsp; "confidence": "Medium",

&nbsp; "notes": ""

}

```



\*\*Executive brief (generated from JSON)\*\*



\* …

\* …

&nbsp; \*\*Action Items\*\*

\* …

&nbsp; \*\*Confidence:\*\* Medium — because …

&nbsp; \*\*Sources:\*\* `...`



---



\## Notes



\* Keep JSON \*\*exactly as returned\*\* (no extra prose in the code block).

\* Keep briefs to \*\*5–7 bullets\*\* + 3 actions. Always include \*\*Confidence\*\* and \*\*Sources\*\*.



````



\### 3) Commit \& push

```powershell

cd "C:\\Users\\Veteran\\ai-agent-mastery-28days"

git add "Week4\_Autonomous\_Strategic\_Agents/Day25/W4D25\_examples.md"

git commit -m "W4D25: add examples template (JSON + executive brief for SWOT/Porter/OKRs)"

git push

````



Want a tiny \*\*post-processor prompt\*\* you can drop into Flowise to turn that JSON into the brief automatically?



