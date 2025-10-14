✅ Day 16 — Local Strategic Agent (Flowise + Ollama + Chroma, Governance-Ready)

Save as: wk03/day16_local_strategic_agent.md

🎯 Purpose

Stand up a private, offline RAG agent that reads your repo, answers with filename citations, and respects your governance context pack (Day 7).

📌 Objectives

Run Flowise locally and wire Ollama + Chroma.

Enforce citations, scope limits, and PII masking.

Export chatflow + notes as auditable assets.

🛠 Agenda (≈30 min)

Install/run → Build chatflow → Test prompts → Export + commit.

Setup (quick)
# Ollama
# pull: phi3:mini, llama3.1:8b, nomic-embed-text

# Flowise (Docker)
docker run -d --name flowise -p 3000:3000 \
  -e FLOWISE_USERNAME=admin -e FLOWISE_PASSWORD=admin \
  -v flowise_data:/root/.flowise flowiseai/flowise

Chatflow (nodes left→right)

Chat Input

Document Loader (globs: **/*.md, **/*.csv)

Text Splitter (chunk 1000 / overlap 150)

Embeddings (Ollama: nomic-embed-text)

Vector Store (Chroma; collection aimastery_wk03_d16)

Retriever (Top-K 5; cosine; threshold 0.35)

Prompt Template (system, below)

LLM (Ollama: phi3:mini → upgrade to llama3.1:8b later)

Chat Output

System Prompt (paste):

You are a Strategic AI Coach grounded ONLY in retrieved repository context.
If the answer is not present, say: “I don’t have that in the repo yet.”
Then suggest which file to add.

Rules:
- Cite filenames (and heading if present) after each relevant bullet: [file.md].
- Keep to concise bullets + a final Action List.
- Mask obvious PII (emails/phones/IDs) as [REDACTED].
- No speculation. No external links unless in the repo.

Tone: executive, plain language, region-aware when relevant.

Test Prompts

“Summarize Week 2 deliverables with file citations.”

“List PII risks mentioned in the repo; where are they documented?”

“Create a Day 16 prep checklist with references.”

📂 Deliverables

wk03/day16/W3D16_flowise_chatflow.json

wk03/day16/W3D16_flowise_screenshot.png

wk03/day16/W3D16_notes.md (model/version, files indexed, Top-K/threshold, sample Q&A)

✅ Rubric

Answers include [file.md] citations

Scope guard returns “don’t have that…” when appropriate

PII masks appear when patterns detected

Notes file complete

📝 Reflection

Where did citations fail?

What Top-K/threshold produced best signal?

Any files to exclude or add?

🧭 Flow (Mermaid)
flowchart LR
  A[Chat Input] --> B[Retriever]
  B --> C[Prompt: Repo-only + Citations]
  C --> D[LLM (Ollama)]
  D --> E[Chat Output]

