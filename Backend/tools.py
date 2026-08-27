"""Tools for the Deep Research AI Agent System."""

from tavily import TavilyClient
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from langchain.tools import tool

import requests
import json


load_dotenv()


# =========================
# SEARCH TOOL
# =========================

@tool
def search(query: str) -> str:
    """
    Search the internet using Tavily API and return top 5 search results.

    Args:
        query: The topic or search query.

    Returns:
        String containing formatted top 5 search results.
    """

    client = TavilyClient()

    try:
        results = client.search(
            query=query,
            max_results=5
        )

        formatted_results = []

        for idx, result in enumerate(results.get("results", []), start=1):

            formatted_results.append({
                "rank": idx,
                "title": result.get("title", ""),
                "snippet": result.get("content", ""),
                "url": result.get("url", "")
            })

        return json.dumps(formatted_results, indent=2)

    except Exception as e:
        return f"Search Error: {str(e)}"


# =========================
# SCRAPER TOOL
# =========================

@tool
def scrape(url: str) -> str:
    """
    Scrape webpage content from a URL using BeautifulSoup.

    Args:
        url: Website URL to scrape.

    Returns:
        Extracted webpage content as string.
    """

    IMPORTANT_TAGS = [
        "h1",
        "h2",
        "h3",
        "p",
        "article"
    ]

    try:

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        extracted_content = []

        for tag in IMPORTANT_TAGS:

            elements = soup.find_all(tag)

            for element in elements:

                text = element.get_text(strip=True)

                if text and len(text) > 30:
                    extracted_content.append(text)

        cleaned_content = "\n\n".join(extracted_content[:50])

        if not cleaned_content:
            return "No meaningful content extracted."

        return cleaned_content

    except requests.RequestException as e:
        return f"Scraping Error: {str(e)}"

    except Exception as e:
        return f"Unexpected Error: {str(e)}"


# =========================
# TESTING
# =========================

if __name__ == "__main__":

    print("\n===== TESTING SEARCH TOOL =====\n")

    search_results = search.invoke(
        "Future of Quantum Computing"
    )

    print(search_results)

    print("\n===== TESTING SCRAPER TOOL =====\n")

    sample_url = "https://en.wikipedia.org/wiki/Quantum_computing"

    scraped_content = scrape.invoke(sample_url)

    print(scraped_content[:1000])