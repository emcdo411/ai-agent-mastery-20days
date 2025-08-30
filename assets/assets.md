# 🎨 W4D28 — Mastery Program Assets

![Status](https://img.shields.io/badge/Day-28-blueviolet?style=for-the-badge)
![Flowise](https://img.shields.io/badge/Flowise-Agent_Builder-green?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-orange?style=for-the-badge)
![Chroma](https://img.shields.io/badge/Chroma-Vector_Store-teal?style=for-the-badge)

---

## 📑 Table of Contents
- [🎯 Purpose](#-purpose)
- [📂 Core Assets](#-core-assets)
- [📦 Deliverables](#-deliverables)
- [🗺 Workflow](#-workflow)

---

## 🎯 Purpose
This folder holds **Day 28 mastery program assets** — foundational files you’ll reference for:
- Explaining **Generative AI vs Agentic AI**  
- Breaking down **Retrieval Augmented Generation (RAG)**  
- Providing visuals, badges, and workflows for presentations or repos  

---

## 📂 Core Assets
- `W4D28_generative_vs_agentic.md` → Deep dive on AI modes  
- `W4D28_rag_deepdive.md` → What RAG is + why it matters  
- `W4D28_assets.md` → This asset index file  

---

## 📦 Deliverables
- Shields.io badges for repo branding  
- Clickable ToC for quick navigation  
- Mermaid workflow diagrams (dark theme)  

---

## 🗺 Workflow

```mermaid
%%{ init: { 'theme': 'dark' } }%%
flowchart LR
    A["🗂 Assets (Day28)"]
    B["🧠 Generative vs Agentic AI"]
    C["📚 RAG Deep Dive"]
    D["🎨 Badges + Visuals"]

    A --> B
    A --> C
    A --> D
````

---

````

---

# 📂 File 2: `W4D28_generative_vs_agentic.md`

```markdown
# 🤖 Generative AI vs Agentic AI

![Topic](https://img.shields.io/badge/Deep_Dive-Generative_vs_Agentic-purple?style=flat-square)

---

## 📑 Table of Contents
- [⚡ Quick Summary](#-quick-summary)
- [🧠 Generative AI](#-generative-ai)
- [🕹 Agentic AI](#-agentic-ai)
- [⚔ Key Differences](#-key-differences)
- [🗺 Workflow](#-workflow)

---

## ⚡ Quick Summary
- **Generative AI**: Models that *generate outputs* (text, image, code).  
- **Agentic AI**: Systems that *act with autonomy*, chaining reasoning, tools, memory, and goals.  

---

## 🧠 Generative AI
- Focus: **output generation** (text, image, video, code).  
- Example: GPT writing an essay or Stable Diffusion creating an image.  
- Limitation: **static** — responds only to a prompt; no memory or tool use.  

---

## 🕹 Agentic AI
- Focus: **autonomous actions** with context + tools.  
- Example: Flowise agent using Ollama to fetch repo data, summarize, then output next steps.  
- Strength: **reasoning + planning + acting** over time.  
- Limitation: More complex setup; requires orchestration (memory, retrievers, routers).  

---

## ⚔ Key Differences

| Feature          | Generative AI             | Agentic AI                    |
|------------------|---------------------------|--------------------------------|
| Output           | Text, code, images        | Actions, plans, multi-step     |
| Context Handling | Single prompt             | Memory + tools + environment   |
| Example          | ChatGPT writing text      | AutoGPT/Flowise RAG pipeline   |
| Dependency       | Model alone               | Model + architecture           |

---

## 🗺 Workflow

```mermaid
flowchart TD
    G["🧠 Generative AI"] --> O["Outputs (text, image, code)"]
    A["🕹 Agentic AI"] --> P["Plans (multi-step)"]
    A --> T["Uses Tools (DBs, APIs)"]
    A --> M["Keeps Memory"]
````

---

````

---

# 📂 File 3: `W4D28_rag_deepdive.md`

```markdown
# 📚 Retrieval Augmented Generation (RAG)

![Topic](https://img.shields.io/badge/Deep_Dive-RAG-blue?style=flat-square)

---

## 📑 Table of Contents
- [⚡ TL;DR](#-tldr)
- [🔍 What RAG Is](#-what-rag-is)
- [📈 Why RAG Matters](#-why-rag-matters)
- [🛠 How RAG Works](#-how-rag-works)
- [🗺 Workflow](#-workflow)

---

## ⚡ TL;DR
RAG = **Retriever + Generator**  
- It *fetches context* from a knowledge base (docs, CSVs, databases)  
- Then passes it into a generative model (LLM)  
- Output = more accurate, grounded answers  

---

## 🔍 What RAG Is
- **Retrieval**: Grabs most relevant chunks from a vector store (e.g., Chroma).  
- **Augmentation**: Adds those chunks into the model’s prompt.  
- **Generation**: LLM uses that context to answer grounded in *real data*.  

---

## 📈 Why RAG Matters
- Prevents hallucinations  
- Makes AI **explainable + auditable**  
- Bridges **static LLM knowledge** with **dynamic external data**  
- Critical for **local-first, privacy-safe AI workflows**  

---

## 🛠 How RAG Works

1. 🧩 **Text Splitter** breaks docs into chunks  
2. 🧬 **Embeddings** turn chunks → vectors  
3. 📂 **Vector Store** indexes & retrieves relevant chunks  
4. 🧠 **LLM** generates answer using both **prompt + retrieved context**  

---

## 🗺 Workflow

```mermaid
%%{ init: { 'theme': 'dark' } }%%
flowchart LR
    D["📂 Documents"]
    S["✂️ Splitter"]
    E["🧬 Embeddings"]
    V["🗃 Vector Store"]
    R["🔎 Retriever"]
    L["🧠 LLM"]

    D --> S --> E --> V
    V --> R --> L
````

---

```

---

✅ Now you’ll have:
- `W4D28_assets.md` → **index** of Day 28 deliverables  
- `W4D28_generative_vs_agentic.md` → **deep dive** with differences + workflow  
- `W4D28_rag_deepdive.md` → **deep dive** on RAG  

---
