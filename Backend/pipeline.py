"""Pipeline for the Deep Research AI Agent System."""

from agents import (
    search_agent,
    scraper_agent,
    writer_chain,
    critic_chain
)


# =========================================================
# MAIN PIPELINE FUNCTION
# =========================================================

def run_research(topic: str):

    # =====================================================
    # INITIAL STATE
    # =====================================================

    state = {
        "topic": topic,
        "search_results": "",
        "scrapped_content": "",
        "report": "",
        "feedback": ""
    }

    print("\n========== STARTING DEEP RESEARCH ==========\n")


    # =====================================================
    # AGENT 1 : SEARCH AGENT
    # =====================================================

    print("Running Search Agent...\n")

    search_response = search_agent.invoke({
        "messages": [
            {
                "role": "system",
                "content": """
                You are a professional research search agent.

                Your task:
                - Search the internet
                - Find top 5 relevant sources
                - Return useful research information
                """
            },
            {
                "role": "user",
                "content": topic
            }
        ]
    })

    # Extract AI response content properly
    search_output = search_response["messages"][-1].content

    # Save in state
    state["search_results"] = search_output

    print("Search Results Saved.\n")


    # =====================================================
    # AGENT 2 : SCRAPER AGENT
    # =====================================================

    print("Running Scraper Agent...\n")

    scraper_response = scraper_agent.invoke({
        "messages": [
            {
                "role": "system",
                "content": """
                You are a professional web scraping agent.

                Your task:
                - Extract useful content from provided URLs
                - Ignore unnecessary webpage content
                - Return clean research information
                """
            },
            {
                "role": "user",
                "content": f"""
                Scrape and extract content from these search results:

                {state["search_results"]}
                """
            }
        ]
    })

    # Extract AI response content properly
    scraper_output = scraper_response["messages"][-1].content

    # Save in state
    state["scrapped_content"] = scraper_output

    print("Scrapped Content Saved.\n")


    # =====================================================
    # AGENT 3 : WRITER CHAIN
    # =====================================================

    print("Running Writer Chain...\n")

    report = writer_chain.invoke({
        "topic": state["topic"],
        "research_content": state["scrapped_content"],
        "links": state["search_results"]
    })

    # Save report
    state["report"] = report

    print("Research Report Generated.\n")


    # =====================================================
    # AGENT 4 : CRITIC CHAIN
    # =====================================================

    print("Running Critic Chain...\n")

    feedback = critic_chain.invoke({
        "report": state["report"]
    })

    # Save feedback
    state["feedback"] = feedback

    print("Feedback Generated.\n")


    # =====================================================
    # FINAL OUTPUT
    # =====================================================

    print("\n========== RESEARCH COMPLETED ==========\n")

    return state


# =========================================================
# TESTING
# =========================================================

if __name__ == "__main__":

    topic = input("Enter Research Topic: ")

    final_state = run_research(topic)

    print("\n========== FINAL REPORT ==========\n")
    print(final_state["report"])

    print("\n========== FEEDBACK ==========\n")
    print(final_state["feedback"])