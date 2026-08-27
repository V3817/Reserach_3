# Deep Research AI Agent System - PRD

## Project Name

Deep Research AI Agent System

---

# 1. Overview

The Deep Research AI Agent System is an autonomous multi-agent research pipeline designed to perform deep internet-based research on a user-provided topic.

The system uses multiple AI agents, external tools, web scraping, and LLM orchestration to:
- Search the web
- Gather relevant sources
- Extract useful information
- Generate a detailed research report
- Critique and score the generated report

The first version will operate entirely through the terminal/CLI.

Future versions will include:
- Streamlit frontend
- LangGraph workflows
- Async pipelines
- PDF exports
- Multi-source intelligence
- Vector memory
- Citation systems

---

# 2. Goal

The goal of this project is to build a modular AI research system capable of:
- Conducting automated internet research
- Synthesizing information into coherent reports
- Evaluating research quality autonomously
- Demonstrating real-world AI agent architecture

This project is intended for:
- AI Engineering portfolio
- Multi-agent systems experimentation
- LLM orchestration learning
- Autonomous research workflow development

---

# 3. Core Features

## Version 1 Features

### Search Agent
- Accepts user topic
- Searches internet using Tavily API
- Returns top 5 relevant search results

### Scraper Agent
- Extracts textual content from URLs
- Uses BeautifulSoup + requests
- Cleans webpage content

### Writer Agent
- Generates detailed research report
- Uses LangChain chains
- Produces structured markdown output

### Critic Agent
- Reviews generated report
- Gives score out of 10
- Provides strengths and weaknesses

### Shared State Management
- Stores outputs from all agents
- Passes data sequentially through pipeline

### CLI Interface
- Runs directly in terminal
- Displays final report and feedback

---

# 4. User Flow

```text
User enters topic
        ↓
Search Agent
        ↓
Search Results stored in state
        ↓
Scraper Agent
        ↓
Scraped content stored in state
        ↓
Writer Agent
        ↓
Generated report stored in state
        ↓
Critic Agent
        ↓
Feedback + score stored in state
        ↓
Final Output Returned
```

---

# 5. System Architecture

## High-Level Architecture

```text
                ┌─────────────────┐
                │     User        │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Search Agent    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Scraper Agent   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Writer Agent    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Critic Agent    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Final Output    │
                └─────────────────┘
```

---

# 6. Tech Stack

## Programming Language
- Python 3.11+

## AI Framework
- LangChain

## LLM Provider
- OpenRouter

## Search API
- Tavily API

## Web Scraping
- BeautifulSoup4
- requests

## Environment Management
- uv

## Configuration
- python-dotenv

## Data Validation
- Pydantic

## Future Frontend
- Streamlit

---

# 7. Project Structure

```text
deep_research/
│
├── agents/
│   ├── search_agent.py
│   ├── scraper_agent.py
│   ├── writer_agent.py
│   └── critic_agent.py
│
├── chains/
│   └── writer_chain.py
│
├── tools/
│   ├── search_tool.py
│   └── scraper_tool.py
│
├── prompts/
│   ├── writer_prompt.py
│   └── critic_prompt.py
│
├── schemas/
│   └── state.py
│
├── pipeline/
│   └── pipeline.py
│
├── utils/
│   ├── llm.py
│   └── helpers.py
│
├── .env
├── .gitignore
├── pyproject.toml
├── README.md
└── main.py
```

---

# 8. Shared State Design

The system uses a shared dictionary state passed across agents.

## State Schema

```python
class ResearchState(TypedDict):
    topic: str
    search_results: list
    scraped_content: list
    report: str
    feedback: str
    score: float
```

---

# 9. Agent Specifications

# 9.1 Search Agent

## Responsibility
Search the internet for relevant sources.

## Inputs
- User topic

## Outputs
- Top 5 search results

## Tools Used
- Tavily API

## Stored State Key

```python
search_results
```

## Result Format

```python
{
    "title": str,
    "url": str,
    "content": str
}
```

---

# 9.2 Scraper Agent

## Responsibility
Extract webpage content from URLs.

## Inputs
- search_results

## Outputs
- Clean webpage text

## Tools Used
- requests
- BeautifulSoup

## Stored State Key

```python
scraped_content
```

## Result Format

```python
{
    "url": str,
    "content": str
}
```

---

# 9.3 Writer Agent

## Responsibility
Generate a structured research report.

## Inputs
- topic
- scraped_content

## Outputs
- Final research report

## Components
- ChatPromptTemplate
- LLM
- StrOutputParser

## Stored State Key

```python
report
```

## Report Requirements
- Structured sections
- Accurate information
- Clear formatting
- Summary and conclusion
- Minimal hallucination

---

# 9.4 Critic Agent

## Responsibility
Evaluate quality of generated report.

## Inputs
- report

## Outputs
- Feedback
- Score

## Stored State Keys

```python
feedback
score
```

## Evaluation Criteria
- Accuracy
- Clarity
- Structure
- Completeness
- Depth
- Relevance

---

# 10. LLM Configuration

## Model Provider
OpenRouter

## Initial Model Recommendation

```text
openai/gpt-4.1-mini
```

## Temperature

```text
0.3
```

## Reason
Lower hallucination and higher factual consistency.

---

# 11. Environment Variables

## .env

```env
OPENROUTER_API_KEY=your_key
TAVILY_API_KEY=your_key
```

---

# 12. Installation Setup

## Initialize Project

```bash
mkdir deep_research
cd deep_research

uv init

uv venv

source .venv/bin/activate
```

---

# 13. Dependency Installation

```bash
uv add langchain
uv add langchain-openai
uv add langchain-community
uv add python-dotenv
uv add beautifulsoup4
uv add requests
uv add tavily-python
uv add pydantic
```

---

# 14. Pipeline Design

## Main Function

```python
run_research(topic: str)
```

## Pipeline Steps

```text
Initialize State
        ↓
Run Search Agent
        ↓
Run Scraper Agent
        ↓
Run Writer Agent
        ↓
Run Critic Agent
        ↓
Return Final State
```

---

# 15. CLI Flow

## User Execution

```bash
python main.py
```

## Terminal Flow

```text
Enter Research Topic:
        ↓
Running Search Agent...
        ↓
Running Scraper Agent...
        ↓
Running Writer Agent...
        ↓
Running Critic Agent...
        ↓
Display Final Report
        ↓
Display Critic Feedback
```

---

# 16. Functional Requirements

## FR-1
System must accept user research topic.

## FR-2
System must search internet sources.

## FR-3
System must scrape webpage content.

## FR-4
System must generate structured report.

## FR-5
System must critique generated report.

## FR-6
System must store outputs in shared state.

## FR-7
System must return final report and feedback.

---

# 17. Non-Functional Requirements

## NFR-1
System should complete execution under 2-3 minutes.

## NFR-2
Architecture must remain modular.

## NFR-3
Agents should be independently replaceable.

## NFR-4
System should support future async upgrades.

## NFR-5
Codebase should remain beginner-friendly.

---

# 18. Error Handling

## Search Failures
- Return empty list
- Retry later

## Scraping Failures
- Skip broken URLs
- Store error logs

## LLM Failures
- Catch API exceptions
- Retry generation

## Timeout Handling
- Use request timeout limits

---

# 19. Future Improvements

# Phase 2 — Frontend

## Streamlit Dashboard
- Topic input box
- Live progress tracking
- Report viewer
- Download report

---

# Phase 3 — LangGraph Migration

## Add
- Stateful workflows
- Conditional routing
- Retry loops
- Parallel execution

---

# Phase 4 — Advanced Intelligence Sources

## Integrations
- Arxiv
- Reddit
- YouTube
- GitHub
- HackerNews
- News APIs

---

# Phase 5 — Autonomous Research System

## Features
- Recursive research
- Self-questioning agents
- Citation validation
- Source ranking
- Multi-step reasoning
- Persistent memory

---

# 20. Risks

## Hallucination Risk
LLMs may fabricate information.

## Scraping Risk
Some websites block scraping.

## Token Explosion
Large webpages can exceed context windows.

## API Costs
Frequent LLM calls increase cost.

---

# 21. Mitigation Strategies

## Hallucination
- Lower temperature
- Use citations
- Add critic validation

## Scraping Issues
- Use retries
- Add Firecrawl later

## Token Limits
- Chunk content
- Summarize before writing

## Cost Optimization
- Use lightweight models initially

---

# 22. Success Metrics

## Technical Success
- End-to-end execution works
- All agents function correctly
- Reports are coherent

## Product Success
- Research quality is useful
- Reports are readable
- System is modular and extensible

## Portfolio Success
- Demonstrates AI engineering capability
- Demonstrates multi-agent architecture
- Demonstrates LLM orchestration

---

# 23. MVP Definition

The MVP is complete when:

- User can enter a topic
- Search agent fetches results
- Scraper extracts webpage text
- Writer generates report
- Critic evaluates report
- Final output displays in terminal

---

# 24. Example Execution

## Input

```text
Topic:
Future of Quantum Computing
```

## Output

```text
1. Detailed Research Report
2. Source Summary
3. Critic Feedback
4. Score out of 10
```

---

# 25. Long-Term Vision

Transform the system into a fully autonomous deep research platform comparable to:
- OpenAI Deep Research
- Gemini Deep Research
- Manus AI
- Perplexity Research Mode

Future capabilities:
- Autonomous planning
- Recursive reasoning
- Multi-agent collaboration
- Source verification
- Persistent memory
- Interactive research sessions
- PDF exports
- Frontend dashboard
- Cloud deployment

---