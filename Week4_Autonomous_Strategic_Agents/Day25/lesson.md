\# Day 25 — Strategic Framework Modules: SWOT, Porter’s, and OKRs (Agent-Callable)



\## 📌 Objective

Add three \*\*reusable strategy modules\*\* to your Flowise agent. Each module:

\- Accepts inputs (company/industry/timeframe/goal)

\- Uses your repo RAG context only (no web)

\- Returns \*\*structured JSON + a short brief\*\*, with \*\*sources\*\* and \*\*confidence\*\*



> Target time: ≤ 30 minutes



---



\## 🛠 What you’ll build

1\) \*\*SWOT Module\*\* (Prompt Template → LLM)  

2\) \*\*Porter’s Five Forces Module\*\*  

3\) \*\*OKR Drafting Module\*\*  

4\) \*\*Router\*\* that selects the module based on user intent  

5\) \*\*Post-processor\*\* that formats JSON → human brief (bullets + actions)



---



\## A) Create Prompt Templates (copy into three Flowise Prompt Template nodes)



\### 1) SWOT Prompt (save text as `W4D25\_swot\_prompt.txt` too)

```



You are a Strategic AI Coach. Use ONLY the retrieved repo context. If evidence is weak, say so.



TASK: Produce a SWOT for:



\* Company/Project: {{company}}

\* Industry: {{industry}}

\* Geography: {{geo}}

\* Timeframe: {{timeframe}}



OUTPUT:

Return valid JSON ONLY with this shape:

{

"company": "{{company}}",

"industry": "{{industry}}",

"timeframe": "{{timeframe}}",

"strengths": \\\[{ "point": "", "evidence": "", "sources": \\\["path/file1.md"] }],

"weaknesses": \\\[{ "point": "", "evidence": "", "sources": \\\[] }],

"opportunities": \\\[{ "point": "", "evidence": "", "sources": \\\[] }],

"threats": \\\[{ "point": "", "evidence": "", "sources": \\\[] }],

"confidence": "High|Medium|Low",

"notes": "one or two caveats"

}



POLICY:



\* Cite filenames/paths from context metadata (e.g., filePath/source).

\* If evidence is missing, include the gap in notes and set confidence Low.



```



\### 2) Porter’s Five Forces (save as `W4D25\_porter\_prompt.txt`)

```



You are a Strategic AI Coach. Use ONLY repo context. No external assumptions.



TASK: Porter’s Five Forces for:



\* Company/Project: {{company}}

\* Industry: {{industry}}

\* Geography: {{geo}}

\* Timeframe: {{timeframe}}



OUTPUT JSON ONLY:

{

"company": "{{company}}",

"industry": "{{industry}}",

"timeframe": "{{timeframe}}",

"forces": \\\[

{ "name":"Threat of New Entrants", "rating": 1-5, "rationale":"", "sources":\\\[] },

{ "name":"Bargaining Power of Suppliers", "rating": 1-5, "rationale":"", "sources":\\\[] },

{ "name":"Bargaining Power of Buyers", "rating": 1-5, "rationale":"", "sources":\\\[] },

{ "name":"Threat of Substitutes", "rating": 1-5, "rationale":"", "sources":\\\[] },

{ "name":"Industry Rivalry", "rating": 1-5, "rationale":"", "sources":\\\[] }

],

"overall": { "rating": 1-5, "comment": "" },

"confidence": "High|Medium|Low",

"notes": ""

}



POLICY:



\* Ratings must be justified with repo citations (filenames/paths).

\* If context insufficient → lower confidence and capture gaps in notes.



```



\### 3) OKR Drafting (save as `W4D25\_okrs\_prompt.txt`)

```



You are a Strategic OKR Coach. Use ONLY repo context (briefs, dashboards, deliverables).



INPUT:



\* Org/Team: {{team}}

\* Horizon: {{timeframe}}

\* Strategic Focus: {{focus}}



OUTPUT JSON ONLY:

{

"team": "{{team}}",

"timeframe": "{{timeframe}}",

"objectives": \\\[

{

"objective": "",

"key\\\_results": \\\[

{ "kr": "", "metric": "", "baseline": "", "target": "", "source\\\_files": \\\[] },

{ "kr": "", "metric": "", "baseline": "", "target": "", "source\\\_files": \\\[] }

],

"owners": \\\["role or placeholder"],

"risks": \\\["risk1","risk2"],

"assumptions": \\\["assumption1"]

}

],

"confidence": "High|Medium|Low",

"notes": "constraints or data gaps"

}



POLICY:



\* Tie KRs to metrics referenced in repo files; cite filenames.

\* If metric baselines are unknown, mark baseline as "unknown" and explain.



```



---



\## B) Wire the \*\*Router\*\* in Flowise

\- Add \*\*If/Else Router\*\* after Chat Input:

&nbsp; - If message contains `swot` → SWOT Prompt → LLM  

&nbsp; - If message contains `porter` or `five forces` → Porter Prompt → LLM  

&nbsp; - If message contains `okr` or `okrs` → OKR Prompt → LLM  

&nbsp; - Else → normal RAG path (Retriever → Prompt → LLM)



> Pass variables as needed: `company, industry, geo, timeframe, team, focus`. If the user didn’t specify, default to repo-wide context (and note that in JSON).



---



\## C) Add a \*\*Post-Processor\*\* (JSON → brief)

Create a Prompt Template \*\*after\*\* the LLM that expects JSON from the module and emits a concise brief:



```



You receive JSON below. Convert to a concise executive brief.



RULES:



\* 5–7 bullets max

\* Add an \*\*Action Items\*\* section (3 bullets)

\* Add \*\*Confidence\*\* and \*\*Sources\*\* (filenames)

\* If fields missing, state the gap plainly.



JSON:

{{module\\\_json}}



```



Connect: Module LLM → Post-Processor Prompt → Final LLM (or just one LLM with function if you prefer). Ensure you feed the raw JSON from the first LLM into `{{module\_json}}`.



---



\## D) Test Prompts

\- “Run a \*\*SWOT\*\* for our Week 2 automation program; timeframe Q4 2025; geography US.”  

\- “Do \*\*Porter’s\*\* for the data-agents training segment; US; next 12 months.”  

\- “Draft \*\*OKRs\*\* for the ‘AI Agent Mastery’ cohort operations; focus = completion \& placements; H1 2026.”



Verify:

\- JSON is valid (no stray text)

\- Sources are repo file paths

\- Confidence matches evidence strength



---



\## 📂 Deliverables

Place in `Week4\_Autonomous\_Strategic\_Agents/Day25/`:

\- `W4D25\_swot\_prompt.txt`

\- `W4D25\_porter\_prompt.txt`

\- `W4D25\_okrs\_prompt.txt`

\- `W4D25\_flowise\_chatflow.json` (export after wiring)

\- `W4D25\_examples.md` (paste 1 example output per module: JSON + brief)



---



\## 🧠 Troubleshooting

\- \*\*LLM outputs text + JSON mixed:\*\* Add “JSON ONLY” and reduce temperature; trim Top-K to 3–4.  

\- \*\*No sources show up:\*\* Ensure retriever exposes `filePath/source` in metadata and that the module prompts demand citations.  

\- \*\*Router misses intent:\*\* Add synonyms (e.g., “framework”, “goals”, “strategy”) or expose explicit buttons in UI (Flowise Chat UI supports quick replies).



\## 🎯 Why this matters

Stakeholders expect \*\*structured strategy\*\* + \*\*evidence\*\*. These modules make your agent board-ready without paid tools.

```



---

