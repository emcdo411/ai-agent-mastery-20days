✅ Day 16 — Local Strategic Agent (Flowise + Ollama + Chroma, Governance-Ready)

Save as: wk03/day16_local_strategic_agent.md

🎯 Purpose

Stand up a private, offline RAG agent that reads your repo, answers with filename citations, and respects your governance context pack (Day 7).

📌 Objectives

Run Flowise locally with Ollama LLM + Chroma vector store.

Enforce repo-only answers, citations, scope limits, and PII masking.

Export chatflow + notes as auditable assets.

⏱ Agenda (≈ 30–45 min)

Install + run → 2) Build chatflow → 3) Test prompts → 4) Export + commit → 5) Reflection.

🧩 Prereqs

Ollama installed and running (phi3:mini, llama3.1:8b, nomic-embed-text).

Your governance pack from Day 7 in the repo (constraints, glossary, PRD links).

🔧 Setup
# Pull models (once)
ollama pull phi3:mini
ollama pull llama3.1:8b
ollama pull nomic-embed-text

# Flowise via Docker
docker run -d --name flowise -p 3000:3000 \
  -e FLOWISE_USERNAME=admin -e FLOWISE_PASSWORD=admin \
  -v flowise_data:/root/.flowise flowiseai/flowise

🛠 Chatflow (nodes left → right)

Chat Input

Document Loader: Local Files — globs: **/*.md, **/*.csv (exclude secrets)

Text Splitter — chunk=1000, overlap=150

Embeddings (Ollama) — nomic-embed-text

Vector Store (Chroma) — collection aimastery_wk03_d16

Retriever — topK=5, cosine, threshold 0.35

Prompt Template — Repo-only + citations + PII mask

LLM (Ollama) — start phi3:mini, upgrade to llama3.1:8b

Chat Output

System Prompt (paste)

You are a Strategic AI Coach grounded ONLY in retrieved repository context.
If the answer is not present, say: “I don’t have that in the repo yet.”
Then suggest which file to add.

Rules:
- Cite filenames (and heading if present) like [path/file.md].
- Use concise bullets + a final Action List.
- Mask obvious PII (emails/phones/IDs) as [REDACTED].
- No speculation. No external links unless in repo sources.

Tone: executive, plain language, region-aware when relevant.

🧪 Test Prompts

“Summarize Week 2 deliverables with file citations.”

“List PII risks mentioned in the repo; where are they documented?”

“Create a Day 16 prep checklist with references.”

📂 Deliverables

wk03/day16/W3D16_flowise_chatflow.json

wk03/day16/W3D16_flowise_screenshot.png

wk03/day16/W3D16_notes.md (model/version, files indexed, K/threshold, sample Q&A)

✅ Rubric

Answers include [path/file.md] citations

Scope guard triggers when content absent

PII masks appear when patterns detected

Notes file complete and reproducible

🧭 Flow (Mermaid)
flowchart LR
  A[Chat Input] --> B[Retriever (Chroma)]
  B --> C[Prompt: Repo-only + Citations + PII Mask]
  C --> D[LLM (Ollama)]
  D --> E[Chat Output]

🧰 Troubleshooting

No citations: expose metadata.filePath in retriever.

Hallucinated files: lower topK to 4, raise threshold to 0.45.

Slow replies: start with phi3:mini.

Index noise: narrow globs; exclude /secrets/.

🔮 Upgrades

Add a pre-index redaction transform (regex masks).

Add Message Prefix node with scope guard text.

Add governance links (constraints.md, glossary.md) to loader paths.
