# Lucy RAG Assessment: Creatine Supplementation Chatbot

A lightweight, professional Retrieval-Augmented Generation (RAG) chatbot built to answer questions strictly based on the provided research paper: *"Creatine Supplementation for Muscle Growth."*

## 🚀 Tech Stack Justification

To ensure high performance, reliability, and accuracy within free-tier constraints, this project utilizes:
* **Backend Framework:** Python + Flask (Lightweight, unopinionated, excellent for microservices).
* **LLM Provider:** **Groq** (`llama-3.3-70b-versatile`). Groq's LPU inference engine provides near-instantaneous token generation, creating a superior real-time chat UX. LLaMA 3.3 70B is highly capable of adhering to strict anti-hallucination system prompts.
* **Embeddings:** **Cohere** (`embed-english-v3.0`). Cohere's v3 models are industry standards for enterprise RAG, utilizing mandatory `input_type` parameters (`search_document` vs `search_query`) to maximize cosine similarity accuracy.
* **Vector Database:** **Pinecone** (Serverless). Provides extremely fast vector similarity search with metadata filtering capabilities, seamlessly integrating with Python.
* **Frontend:** Vanilla HTML/JS/CSS with Bootstrap 5. Kept minimal and dependency-free to demonstrate clean API integration and separation of concerns.

---

## 🧠 Architectural Decisions (As requested)

**Chunking Strategy**  
The PDF is processed using `PyMuPDF` (fitz). The text is split using a sliding window chunking strategy with a `chunk_size` of 800 characters and an `overlap` of 150 characters. Because scientific papers feature complex, multi-clause sentences, the overlap ensures that semantic context isn't severed between chunks. Each chunk is enriched with `page_number` metadata prior to embedding, enabling the LLM to provide accurate `[Page X]` citations.

**Retrieval Settings**  
The system embeds the user's query and searches Pinecone for the `top_k=10` most similar chunks. A similarity threshold logic (`score > 0.2`) is implemented to silently discard highly irrelevant chunks. The retrieved chunks are formatted into a single context string and injected into the LLM's system prompt. If the user asks an out-of-domain question, the strict system prompt forces the LLM to refuse to answer, preventing hallucinations.

**Conversation Memory**  
Session memory is implemented using a lightweight, file-based JSON storage system mechanism (`sessions/{session_id}.json`). When a user connects to the frontend, a unique UUID is generated. All subsequent user queries and assistant responses are appended to this file. During retrieval, the last 4 interactions are injected into the LLM's message array, allowing it to maintain conversational context (e.g., resolving pronouns in follow-up questions) without overflowing the context window.

---

## 🛠️ Setup & Run Instructions

### 1. Prerequisites
Ensure you have Python 3.9+ installed.

### 2. Environment Variables
Create a `.env` file in the root directory and add the following keys:
```env
COHERE_API_KEY=your_cohere_key_here
PINECONE_API_KEY=your_pinecone_key_here
PINECONE_INDEX_NAME=lucy-rag-index
GROQ_API_KEY=your_groq_key_here
(Note: Ensure your Pinecone index is created with 1024 dimensions and the cosine metric).
3. Installation
Activate a virtual environment and install the required packages:
code
Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
4. Running the Application
Start the Backend API:
code
Bash
python run.py
The Flask server will start on http://127.0.0.1:5000.
Start the Frontend:
Because the API handles CORS natively, no frontend build step or web server is required. Simply open your file explorer, navigate to the frontend/ directory, and double-click index.html to open it in your browser.
5. Usage & Testing Flow
Open the UI via index.html.
In the "Document Ingestion" panel, click "Choose File" and select the provided creatine_paper.pdf.
Click Upload & Process PDF. Wait for the success message (the backend is parsing, chunking, embedding, and upserting to Pinecone).
Use the Chat Interface to ask questions (e.g., "What does the paper say about older adults?" or "What are the dosage strategies?").
Notice the [Page X] citations and the chatbot's ability to remember previous questions!
code
Code
---


git add .
git commit -m "Complete RAG implementation: Backend, Frontend, and Documentation"
git push origin main