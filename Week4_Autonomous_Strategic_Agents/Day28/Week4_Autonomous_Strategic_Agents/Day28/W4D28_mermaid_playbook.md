#  W4D28 — Mermaid Playbook: Making Advanced Diagrams & Strategic Templates for Ethiopian NGOs

##  Purpose  
As the **AI Strategist Lead**, your job is to equip Ethiopian nonprofits with **best-in-class visual tools** and actionable prompts. This playbook shows two things:

1. **How to write advanced Mermaid diagrams** that render cleanly on GitHub.  
2. **Five essential AI prompt templates** tailored to common nonprofit challenges in Ethiopia.

---

## 1. Meta Prompt for Clean GitHub-Compatible Mermaid

Use this core prompt to generate diagrams that are **renderable in GitHub README files** (avoiding syntax pitfalls like unsupported symbols or breaks).

```text
You are an AI Strategist Lead.  
Help me generate an **advanced, boardroom-ready Mermaid flowchart** that works in GitHub Markdown.

GUIDELINES:
- Use only clean Mermaid syntax: no `%`, `~`, Unicode arrows, or parentheses that break parsing.
- Label nodes clearly with words (e.g., "Process", "Decision", "Yes", "No").
- Use `<br/>` for multi-line node labels.
- Include multiple branches (e.g., Yes⁄No, Safe⁄At Risk).
- At the end, give 2–3 short narrative bullets for explaining the diagram to boards or funders.

EXAMPLE INPUT:
- Structure: "Client Intake" → "Service Delivery" → "Follow-Up"  
- Branch: "Insurance Payment OK?"  

EXPECTED OUTPUT:
- A valid Mermaid diagram block
- Narrative bullets for stakeholder presentation
````

---

## 2. 5 Strategic Prompts for Ethiopian Nonprofits

Use these as templates for mission-critical AI workflows. Replace placeholders or adapt domains as needed.

### Prompt 1: Program Theory of Change

```text
Create a Mermaid flowchart mapping:
Input → Activity → Output → Outcome → Impact  
Context: Ethiopian rural education program  
Include risk nodes like “Funding Delay” or “Transport Issues”.  
Also provide 2 narrative bullets for board storytelling.
```

### Prompt 2: Donor Funds Flow & Accountability

```text
Diagram how donor funds move:
Donor → HQ → Regional Office → Field Team → Beneficiaries  
Add checkpoints: “Audit”, “Field Verification”, “Community Feedback”.  
Highlight leakage risks.  
Include narrative bullets explaining governance structure.
```

### Prompt 3: Maternal Health Service Journey

```text
Map the patient path:
Community → Clinic Visit → Referral Hospital → Outcome  
Decision nodes: “Transport Available?”, “Supplies In Stock?”  
Mark high risk nodes in red.  
Add a narrative for health leadership brief.
```

### Prompt 4: Emergency Response Flowchart

```text
Flow: Weather Alert → Mobilization → Resource Dispatch → Community Delivery  
Branch: If “Insufficient Resources” → “Request Support from Donors”  
Include quick narrative bullets for government briefing.
```

### Prompt 5: M\&E Feedback Loop

```text
Visualize data cycle:
Collect Data → Clean → Analyze → Report → Act → Collect Data  
Include checks: “Data Quality OK?”, “Community Feedback Integrated?”  
Add round-trip flow arrow.  
Add narrative bullets for internal performance review.
```

---

## Why This Is Best-in-Class

* **GitHub‑safe syntax** avoids crashing render engines (based on GitHub’s current Mermaid version) ([github.blog][1], [docs.github.com][2], [reddit.com][3])
* **Clear labels** and `<br/>` ensure readability even in dense charts
* **Narrative bullets** translate visuals into strategic storytelling
* **Contextual relevance** aligns with Ethiopian nonprofit needs

---

## Sample Use-Case: Maternal Health Prompt + Output

**Prompt:**

```
Diagram the patient journey for maternal health services in rural Ethiopia:
Community → Clinic → Referral Hospital → Outcome  
Include decision nodes: "Transport Available?", "Supplies In Stock?".  
Highlight high-risk points. Add narrative bullets for a donor pitch.
```

**AI Response (example):**

```mermaid
flowchart TD
  %% ===== Nodes =====
  C([Community Patient]):::start
  D1{Transport<br/>available?}:::decision
  CHW[Community Health Worker<br/>triage & advice]:::process
  CH[Primary Clinic<br/>nurse assessment]:::process
  D2{Essential supplies<br/>in stock?}:::decision
  TRIAGE{Meets referral<br/>criteria?}:::decision
  HH[Referral Hospital<br/>OB/GYN or surgery]:::process
  OUT[Positive health outcome]:::good
  RISK_DELAY([Delay — high risk]):::risk
  RISK_STOCK([Stockout — high risk]):::risk
  NEG[Adverse outcome]:::bad
  MIT_TRAN[Mitigation:<br/>transport voucher / ambulance]:::mitigation
  MIT_STOCK[Mitigation:<br/>borrow kit / alternate clinic]:::mitigation
  RESTOCK[Restock request<br/>LMIS ticket raised]:::process
  QA[Quality review<br/>M&M / case audit]:::review
  FEED[Community feedback<br/>and health ed]:::feedback

  %% ===== Main Flow =====
  C --> D1
  D1 -->|Yes| CH
  D1 -->|No| CHW
  CHW --> MIT_TRAN
  MIT_TRAN --> CH
  CH --> D2

  %% Supplies decision
  D2 -->|Yes| TRIAGE
  D2 -->|No| RISK_STOCK --> MIT_STOCK --> RESTOCK --> CH
  RISK_STOCK --> NEG

  %% Referral decision
  TRIAGE -->|Yes| HH
  TRIAGE -->|No| CHW

  %% Outcomes
  HH --> OUT
  CHW --> OUT
  RISK_DELAY --> NEG
  CHW -. if unresolved .-> RISK_DELAY

  %% Feedback & Learning Loops
  OUT -. success factors .-> QA
  NEG -. root cause .-> QA
  QA -. actions & SOP updates .-> CH
  QA -. transport policy updates .-> CHW
  OUT -. community trust .-> FEED -.-> C
  NEG -. risk communication .-> FEED -.-> C

  %% ===== Styles =====
  classDef start fill:#cfe8ff,stroke:#0062cc,stroke-width:2px,color:#002a5a;
  classDef decision fill:#fff3cd,stroke:#8c6d1f,stroke-width:2px,color:#3d2f00;
  classDef process fill:#e9ecef,stroke:#495057,stroke-width:1.5px,color:#212529;
  classDef mitigation fill:#e8f7ff,stroke:#0aa2c0,stroke-width:2px,color:#044e54,stroke-dasharray: 4 3;
  classDef review fill:#ede7f6,stroke:#5e35b1,stroke-width:2px,color:#311b92;
  classDef feedback fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1,stroke-dasharray: 5 4;
  classDef risk fill:#fdecea,stroke:#b71c1c,stroke-width:2px,color:#5d0000;
  classDef good fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px,color:#0b3d0b;
  classDef bad fill:#ffebee,stroke:#c62828,stroke-width:2px,color:#6a1b1b;


```

**Narrative:**

* Delays at the transport and stock availability nodes risk patient outcomes.
* Highlight investments in transport logistics and supply chain as mitigation.

---

Place this file as `Week4_Autonomous_Strategic_Agents/Day28/W4D28_mermaid_playbook.md` in your repo, and it's ready to empower learners.

Let me know if you'd like me to include a rendered sample using real Ethiopian program data or prepare a slide deck snippet for quick deployment!

[1]: https://github.blog/developer-skills/github/include-diagrams-markdown-files-mermaid/?utm_source=chatgpt.com "Include diagrams in your Markdown files with Mermaid"
[2]: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams?utm_source=chatgpt.com "Creating Mermaid diagrams"
[3]: https://www.reddit.com/r/github/comments/100mbuh/mermaid_diagram_not_working/?utm_source=chatgpt.com "Mermaid diagram not working : r/github"
