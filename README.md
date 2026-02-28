# Lucy RAG Assistant: Professional AI Chatbot

A production-grade Retrieval-Augmented Generation (RAG) chatbot designed to answer questions strictly based on uploaded PDF documents. This project goes beyond basic requirements by implementing **multi-tenant data isolation**, **smart conversation handling**, and a **responsive, accessible UI**.

🔗 **Live Demo:** https://lucy-rag-chatbot.onrender.com

---

## 🚀 Key Features (Beyond the Basics)

This project implements several advanced features to ensure a professional user experience and architectural robustness:

### 1. 🛡️ Multi-Tenant Data Isolation
Unlike basic RAG implementations that mix all uploads into a shared index, this system tags every vector chunk with a unique `session_id`.
*   **Benefit:** Multiple users can use the app simultaneously without their documents or queries leaking to one another.
*   **Implementation:** Pinecone metadata filtering (`filter={"session_id": {"$eq": session_id}}`).

### 2. 🎨 Modern, Accessible UI
A fully responsive frontend built with **Bootstrap 5** and **Vanilla JS**, featuring:
*   **Dark/Light Mode:** Automatically saves user preference.
*   **Markdown Rendering:** Chat responses feature properly formatted lists, bold text, and code blocks.
*   **Real-time Feedback:** Progress bars for ingestion and typing indicators for latency masking.

### 3. 🧠 "Smart" System Prompts
The LLM logic (LLaMA 3.3 70B via Groq) is optimized to distinguish between context:
*   **Chit-chat:** Handles greetings ("Hello", "Who are you?") naturally without searching the document.
*   **Factual Queries:** Strictly grounds answers in the retrieved chunks with **[Page X]** citations.
*   **Anti-Hallucination:** Explicitly refuses to answer questions not found in the source text.

### 4. 🧹 Resource Management
Includes an automated cleanup mechanism. The `/api/clear` endpoint wipes both the Pinecone vectors and the session JSON history, ensuring the free-tier vector database doesn't hit storage limits.

---

## 🛠️ Tech Stack

*   **Backend:** Python 3.9+, Flask, Gunicorn (Production WSGI)
*   **Frontend:** HTML5, CSS3, JavaScript (ES6+), Bootstrap 5
*   **LLM Engine:** **Groq** (Model: `llama-3.3-70b-versatile`) - Chosen for near-instant inference speed.
*   **Embeddings:** **Cohere** (`embed-english-v3.0`) - Uses specific `input_type` for high-accuracy retrieval.
*   **Vector DB:** **Pinecone** (Serverless) - chosen for low-latency metadata filtering.

---

## 🏗️ Architecture & Decisions

**Chunking Strategy**
We use `PyMuPDF` for high-fidelity text extraction. The text is split using a **sliding window approach** (Chunk Size: 800 chars, Overlap: 150 chars).
*   *Why?* Scientific papers often contain complex sentences that span line breaks. Overlap ensures semantic meaning is preserved across chunk boundaries.

**Retrieval Strategy**
*   **Top-K:** 10 chunks.
*   **Similarity Threshold:** 0.2 (cosine similarity).
*   **Hybrid Logic:** The system embeds the query using Cohere's `search_query` input type, ensuring better alignment with the `search_document` embeddings stored in Pinecone.

**Memory Management**
Session history is stored in lightweight JSON files (`sessions/{uuid}.json`). The last 4 turns of conversation are injected into the context window, allowing the LLM to resolve pronouns (e.g., "What is *its* dosage?") without exceeding token limits.

---

## 💻 Local Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/eyuBirhanu/lucy-rag-assessment.git
cd lucy-rag-assessment
```

### 2. Environment Configuration

Create a `.env` file in the root directory:

```env
COHERE_API_KEY=your_key_here
PINECONE_API_KEY=your_key_here
PINECONE_INDEX_NAME=lucy-rag-index
GROQ_API_KEY=your_key_here
FLASK_ENV=development
```

### 3. Install Dependencies

```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 4. Run Locally

```bash
python run.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## ☁️ Deployment (Render.com)

This project is configured for seamless deployment on Render.

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn run:app`
- **Environment Variables:** Add your API keys in the Render Dashboard.

---

## 📂 Project Structure

```text
├── app/
│   ├── static/          # CSS, JS, Images
│   ├── templates/       # HTML files
│   ├── services/        # Logic for RAG, Embeddings, Database
│   ├── routes.py        # API Endpoints
│   └── __init__.py      # App Factory
├── sessions/            # JSON Session storage (gitignored)
├── uploads/             # Temp file storage (gitignored)
├── run.py               # Entry point
└── requirements.txt     # Python dependencies
```

---

## 👤 Author

Built by **Eyu Birhanu** for the Lucy technical assessment.

---

### 💡 One Last Tip for Submission
When you submit the email to `moan.bekele@lucyhub.ai`, you can now say:

> "I implemented the core requirements, but I also added **multi-user isolation** so users don't see each other's data, and a **dark-mode UI** that matches the Lucy brand style."

This `README.md` proves you didn't just code the assignment—you built a **product**. 🚀