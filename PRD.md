# PRD — Deep Research AI

## Overview

Deep Research AI is a multi-agent autonomous research system that performs deep internet research on a user-provided topic. The platform searches the web, scrapes relevant content, generates a structured AI-written report, critiques the generated output, and presents the final research inside a modern React frontend.

---

# Objective

Build a production-style AI research assistant capable of:
- Searching the web
- Extracting useful information
- Generating detailed reports
- Evaluating report quality
- Providing downloadable research documents

---

# Core Features

- AI-powered research pipeline
- Tavily web search integration
- Web scraping using BeautifulSoup
- Structured markdown report generation
- Critic/evaluator AI agent
- React frontend UI
- FastAPI backend
- PDF export
- Markdown export
- Source visualization

---

# User Flow

```text
User enters topic
        ↓
Search Agent
        ↓
Scraper Agent
        ↓
Writer Chain
        ↓
Critic Chain
        ↓
Frontend displays:
- Report
- Feedback
- Sources
```

---

# Architecture

```text
React Frontend
        ↓
FastAPI Backend
        ↓
Research Pipeline
        ↓
LLM Agents + Tools
```

---

# Tech Stack

## Frontend
- React
- Axios
- React Markdown

## Backend
- FastAPI
- LangChain
- Mistral AI
- Tavily API
- BeautifulSoup

## Tooling
- uv
- Vite
- Python

---

# AI Agents

## Search Agent
Searches the web for relevant sources.

## Scraper Agent
Extracts webpage content from URLs.

## Writer Chain
Generates structured research reports.

## Critic Chain
Evaluates and critiques generated reports.

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
  "report": "...",
  "feedback": "...",
  "sources": []
}
```

---

# Future Improvements

- Streaming responses
- LangGraph workflows
- Async scraping
- Citation system
- Research history
- Authentication
- Vector memory
- Multi-agent planning

---

# Deployment

## Frontend
- Vercel

## Backend
- Railway

---