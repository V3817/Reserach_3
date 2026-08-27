"""Agents for the Deep Research AI Agent System."""

from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from tools import search, scrape


load_dotenv()


# =========================================================
# LLM CONFIGURATION
# =========================================================

llm = ChatOpenAI(
    model="mistral-medium-latest",
    base_url="https://api.mistral.ai/v1",
    api_key=os.getenv("MISTRAL_API_KEY"),
    temperature=0.3
)


# =========================================================
# AGENT 1 : SEARCH AGENT
# =========================================================

search_agent = create_agent(
    model=llm,
    tools=[search]
)


# =========================================================
# AGENT 2 : SCRAPER AGENT
# =========================================================

scraper_agent = create_agent(
    model=llm,
    tools=[scrape]
)


# =========================================================
# AGENT 3 : WRITER LCEL CHAIN
# =========================================================

WRITER_SYSTEM_PROMPT = """
You are an expert AI research writer.

Your task:
- Create a detailed research report
- Use topic, research content, and links
- Use headings and subheadings
- Keep report factual and structured
- Add conclusion and future outlook
"""


writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        WRITER_SYSTEM_PROMPT
    ),
    (
        "human",
        """
        Topic:
        {topic}

        Combined Research:
        {research_content}

        Source Links:
        {links}

        Generate a professional deep research report.
        """
    )
])


writer_chain = (
    writer_prompt
    | llm
    | StrOutputParser()
)


# =========================================================
# AGENT 4 : CRITIC LCEL CHAIN
# =========================================================

CRITIC_SYSTEM_PROMPT = """
You are a senior research evaluator.

Your task:
- Review the report
- Give score out of 10
- Identify strengths
- Identify weaknesses
- Suggest improvements
"""


critic_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        CRITIC_SYSTEM_PROMPT
    ),
    (
        "human",
        """
        Evaluate the following report:

        {report}
        """
    )
])


critic_chain = (
    critic_prompt
    | llm
    | StrOutputParser()
)


# =========================================================
# TESTING
# =========================================================

if __name__ == "__main__":

    print("\n========== SEARCH AGENT ==========\n")

    search_result = search_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": "Future of Quantum Computing"
            }
        ]
    })

    print(search_result)


    print("\n========== SCRAPER AGENT ==========\n")

    scrape_result = scraper_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": "https://en.wikipedia.org/wiki/Quantum_computing"
            }
        ]
    })

    print(scrape_result)


    print("\n========== WRITER CHAIN ==========\n")

    report = writer_chain.invoke({
        "topic": "Future of Quantum Computing",
        "research_content": """
        Quantum computing uses qubits and quantum mechanics
        to solve complex problems faster than classical computers.
        """,
        "links": """
        https://en.wikipedia.org/wiki/Quantum_computing
        """
    })

    print(report[:1500])


    print("\n========== CRITIC CHAIN ==========\n")

    feedback = critic_chain.invoke({
        "report": report
    })

    print(feedback)