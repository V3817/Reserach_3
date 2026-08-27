# Deep Research AI

An autonomous multi-agent AI research system that performs deep internet research, extracts relevant information, generates structured reports, critiques the generated output, and provides downloadable research reports through a modern React frontend.

---

# Features

- Multi-agent AI research pipeline
- Tavily-powered web search
- Web scraping using BeautifulSoup
- AI-generated structured research reports
- Critic/evaluator agent with feedback
- FastAPI backend
- React frontend
- Markdown rendering
- PDF report download
- Markdown export
- Source visualization
- Modular architecture
- Environment variable support
- Production-ready structure

---

# Architecture

```text
React Frontend
        ↓
FastAPI Backend
        ↓
Research Pipeline
        ↓
Search Agent
        ↓
Scraper Agent
        ↓
Writer Chain
        ↓
Critic Chain
```

---

# Tech Stack

## Frontend
- React
- Axios
- React Markdown
- jsPDF
- html2canvas

## Backend
- FastAPI
- LangChain
- Mistral AI
- Tavily API
- BeautifulSoup
- Requests

## Environment & Tooling
- uv
- Python 3.10+
- Vite

---

# Project Structure

```text
deep_research_ai/
│
├── backend/
│   ├── agents.py
│   ├── pipeline.py
│   ├── tools.py
│   ├── main.py
│   ├── requirements.txt
│   ├── pyproject.toml
│   ├── uv.lock
│   ├── .env
│   └── routers/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── .env
│
└── README.md
```

---

# Setup Instructions

# 1. Clone Repository

```bash
git clone <your_repo_url>

cd deep_research_ai
```

---

# 2. Backend Setup

## Navigate to backend

```bash
cd backend
```

## Create virtual environment

```bash
uv venv
```

## Activate environment

### macOS/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## Install dependencies

```bash
uv sync
```

---

# 3. Backend Environment Variables

Create `.env` inside backend:

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
FRONTEND_URL=http://localhost:5173
```

---

# 4. Run Backend

```bash
uv run uvicorn main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# 5. Frontend Setup

## Navigate to frontend

```bash
cd frontend
```

---

## Install dependencies

```bash
npm install
```

---

# 6. Frontend Environment Variables

Create `.env` inside frontend:

```env
VITE_API_URL=http://127.0.0.1:8000
```

---

# 7. Run Frontend

```bash
npm run dev
```

Frontend runs at:

```text
http://localhost:5173
```

---

# API Endpoint

## POST `/research`

### Request

```json
{
  "topic": "Future of Quantum Computing"
}
```

### Response

```json
{
  "topic": "Future of Quantum Computing",
  "report": "...",
  "feedback": "...",
  "sources": []
}
```

---

# Agents Overview

# Search Agent
- Searches web using Tavily
- Retrieves top relevant sources

# Scraper Agent
- Scrapes webpage content
- Extracts useful text data

# Writer Chain
- Generates structured research report
- Uses LCEL architecture

# Critic Chain
- Evaluates report quality
- Provides feedback and scoring

---

# Current Features

- Deep web research
- Autonomous AI workflow
- Structured markdown reports
- Report critique system
- PDF export
- Markdown export
- Source cards
- Modern dark UI

---

# Future Improvements

- Streaming responses
- LangGraph workflows
- Async scraping
- Research memory
- Citation support
- User authentication
- Database storage
- Research history
- Multi-agent planning
- Cloud deployment improvements

---

# Deployment

## Frontend
Recommended:
- Vercel

## Backend
Recommended:
- Railway

---

# Environment Files

## Frontend

```env
VITE_API_URL=
```

## Backend

```env
MISTRAL_API_KEY=
TAVILY_API_KEY=
FRONTEND_URL=
```

---

# Security Notes

- Never commit `.env`
- Never expose API keys
- Use environment variables for deployment
- Configure CORS properly

---

# License

MIT License

---

# Author

Aryal Katkar

---

# Screenshots

Add screenshots of:
- Home UI
- Generated report
- Sources section
- PDF export

---

# Acknowledgements

- LangChain
- Mistral AI
- Tavily
- FastAPI
- React
- BeautifulSoup
- Vite