# 🚀 STARTWISE - AI Startup Innovation Evaluation Platform

STARTWISE is an AI-powered web application that evaluates startup ideas using a multi-agent architecture. It analyzes different aspects of a startup such as the problem, market, business model, technical feasibility, and risk. The platform also recommends relevant government startup schemes using Retrieval-Augmented Generation (RAG).

---

## ✨ Features

- 🤖 Multi-Agent AI Evaluation
- 📊 Startup Score Dashboard
- 💡 Innovation Suggestions
- 💰 Investment Recommendation
- 🏛️ Government Scheme Recommendation (RAG)
- ⚡ Groq Llama 3.3 70B Integration
- 🎨 Modern React + Tailwind Frontend
- 🚀 FastAPI Backend

---

# 🏗️ Tech Stack

### Frontend

- React
- Tailwind CSS
- Axios

### Backend

- Python
- FastAPI
- Uvicorn

### AI

- Groq API
- Llama 3.3 70B

### RAG

- ChromaDB
- Sentence Transformers
- all-MiniLM-L6-v2

---

# 📂 Project Structure

```
startup-evaluator/

├── backend/
│   ├── agents/
│   ├── data/
│   ├── rag/
│   ├── services/
│   ├── orchestrator/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── ...
│
└── README.md
```

---

# ⚙️ Backend Setup

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/startup-evaluator.git

cd startup-evaluator
```

---

## 2. Create Virtual Environment

Windows

```bash
cd backend

python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create .env

Inside the backend folder create

```
.env
```

Add

```
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

You can get a free API key from

https://console.groq.com/

---

## 5. Start Backend

```bash
uvicorn main:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

---

# 💻 Frontend Setup

Open a new terminal

```bash
cd frontend
```

Install packages

```bash
npm install
```

Run frontend

```bash
npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

# 🏛️ RAG Setup

The project uses ChromaDB to store government startup schemes.

When the backend starts for the first time, the database is automatically created if it doesn't already exist.

Government schemes are stored in

```
backend/data/government_schemes.json
```

The vector database is stored in

```
backend/chroma_db/
```

---

# 🚀 How It Works

```
User

↓

React Frontend

↓

FastAPI Backend

↓

Orchestrator

↓

Multi-Agent Evaluation

↓

RAG Retrieval

↓

Groq LLM

↓

Final Startup Evaluation Report
```

---

# 🤖 AI Agents

- Problem Agent
- Market Agent
- Business Agent
- Technical Agent
- Risk Agent
- Innovation Agent
- Investment Committee Agent

---

# 📊 Evaluation Includes

- Overall Startup Score
- Problem Analysis
- Market Analysis
- Business Model Evaluation
- Technical Feasibility
- Risk Analysis
- Innovation Suggestions
- Investment Recommendation
- Government Scheme Recommendations

---

<!-- # 📸 Screenshots

(Add screenshots here) -->

<!-- --- -->

# ❗ Troubleshooting

### Backend takes time to start

The backend loads the SentenceTransformer embedding model during startup. The first startup may take a few seconds as the model is loaded into memory.

---

### Government schemes are not showing

The application automatically creates the ChromaDB vector database if it does not exist.

If the problem persists:

1. Delete the `backend/chroma_db/` folder.
2. Restart the backend.
3. The database will be recreated automatically.

---

### Invalid Groq API Key

Ensure that your `.env` file contains a valid key:

```text
GROQ_API_KEY=YOUR_API_KEY
```

---

### Frontend cannot connect to backend

Make sure the backend is running on

```
http://127.0.0.1:8000
```

before starting the frontend.

---


# 👨‍💻 Developed By

Ch.Dhanush