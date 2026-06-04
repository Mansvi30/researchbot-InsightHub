import requests
import xml.etree.ElementTree as ET
from scholarly import scholarly

class DataLoader:
    def __init__(self):
        print("DataLoader Init")

    def fetch_arxiv_papers(self, query):
        """
        Fetches top 5 research papers from ArXiv based on the user query.
        """
        def search_arxiv(search_query):
            """Helper function to query ArXiv API."""
            url = f"http://export.arxiv.org/api/query?search_query=all:{search_query}&start=0&max_results=5"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    root = ET.fromstring(response.text)
                    return [
                        {
                            "title": entry.find("{http://www.w3.org/2005/Atom}title").text.strip().replace('\n', ' '),
                            "summary": entry.find("{http://www.w3.org/2005/Atom}summary").text.strip(),
                            "link": entry.find("{http://www.w3.org/2005/Atom}id").text.strip()
                        }
                        for entry in root.findall("{http://www.w3.org/2005/Atom}entry")
                    ]
            except Exception as e:
                print(f"Error fetching from ArXiv: {e}")
            return []

        return search_arxiv(query)

    def fetch_google_scholar_papers(self, query):
        """
        Fetches top 5 research papers from Google Scholar.
        """
        papers = []
        try:
            search_results = scholarly.search_pubs(query)
            for i, paper in enumerate(search_results):
                if i >= 5:
                    break
                papers.append({
                    "title": paper["bib"]["title"],
                    "summary": paper["bib"].get("abstract", "No summary available"),
                    "link": paper.get("pub_url", "No link available")
                })
        except Exception as e:
            print(f"Error fetching from Google Scholar: {e}")
        return papers