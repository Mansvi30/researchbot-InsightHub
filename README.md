Agent Definitions
summarizer_agent: Instructed strictly to distill complex academic text into clear, objective overviews without disclosing thought processes.

advantages_disadvantages_agent: Ingests summaries to contrast the strengths and structural/methodological flaws of each research contribution.

🚀 Getting Started
Follow these steps to set up and run the Virtual Research Assistant locally.

1. Prerequisites
Python 3.9 or higher installed on your machine.

A Groq API Key. You can obtain one for free by creating an account at the Groq Developer Console.

2. Clone or Set Up Your Project Directory
Ensure your files match the project structure shown above. Navigate into your project folder:

Bash
cd virtual-research-assistant
3. Set Up a Virtual Environment (Recommended)
Isolate your dependencies using a Python virtual environment:

Bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\\Scripts\\activate
# On macOS/Linux:
source venv/bin/activate
4. Install Dependencies
Install all the underlying required libraries including AutoGen, Streamlit, and environment management tools:

Bash
pip install streamlit pyautogen python-dotenv requests scholarly
5. Configure Environment Variables
Create a file named .env in the root directory of the project to store your secret API key safely:

Code snippet
GROQ_API_KEY=your_actual_groq_api_key_here
6. Run the Application
Boot up the local Streamlit web server by running:

Bash
streamlit run app.py
Once executed, your terminal will confirm initialization, and the dashboard will automatically open in your default web browser at http://localhost:8501.

💡 Usage Guide
Enter a Topic: Open the dashboard and input any academic domain, theory, or keyword (e.g., "Retrieval-Augmented Generation", "Quantum Computing Architecture", or "Graph Neural Networks").

Search and Analyze: Click the Search & Analyze button.

Review Results: The application will load the top matching papers. Under each paper title, explore the Concise Summary and Pros & Cons Analysis tabs compiled in real-time by your autonomous AI research team.

🛡️ License
This project is open-source and available under the MIT License.
"""

with open("README.md", "w", encoding="utf-8") as f:
f.write(readme_content)

print("README.md written successfully.")

Your `README.md` markdown file is ready
[file-tag: code-generated-file-0-1780595312376954031]

Here is the complete source content generated for your project's **README.md** file, which acts as the professional documentation for GitHub or your project folder:

```markdown
# 📚 Virtual Research Assistant

An AI-powered multi-agent system built using **AutoGen**, **Streamlit**, and **Groq (Llama 3.3)** that automates the process of finding, summarizing, and analyzing academic research papers. 

The application queries open research repositories (like ArXiv), orchestrates a team of specialized large language model (LLM) agents to break down the papers, and delivers structured insights directly to a clean web dashboard.

---

## 🎯 Features

- **Automated Paper Fetching:** Dynamically queries the ArXiv API based on user-defined search topics or keywords.
- **Multi-Agent Orchestration:** Utilizes Microsoft AutoGen to manage a team of collaborative AI agents powered by Groq's high-speed inference.
- **Specialized Summarization Agent:** Reads through dense scientific abstracts and extracts concise, human-readable summaries without unnecessary fluff.
- **Critique & Analysis Agent:** Evaluates the generated summaries to automatically itemize the core advantages and disadvantages of each paper in a structured, pointwise format.
- **Interactive UI Dashboard:** A polished Streamlit interface that organizes findings into neat, side-by-side tabs for rapid literature reviews.

---

## 🏗️ Project Architecture

The workspace is organized into modular components separating the UI, agent configurations, and data retrieval layers:

```text
virtual-research-assistant/
│
├── app.py              # Streamlit frontend, UI layout, and execution flow
├── agents.py           # AutoGen agent initializations, prompts, and wrapper functions
├── data_loader.py      # Core data fetching logic for interacting with ArXiv and Scholar APIs
└── .env                # Local environment file containing secret API credentials (ignored by git)
Agent Definitions
summarizer_agent: Instructed strictly to distill complex academic text into clear, objective overviews without disclosing thought processes.

advantages_disadvantages_agent: Ingests summaries to contrast the strengths and structural/methodological flaws of each research contribution.

🚀 Getting Started
Follow these steps to set up and run the Virtual Research Assistant locally.

1. Prerequisites
Python 3.9 or higher installed on your machine.

A Groq API Key. You can obtain one for free by creating an account at the Groq Developer Console.

2. Clone or Set Up Your Project Directory
Ensure your files match the project structure shown above. Navigate into your project folder:

Bash
cd virtual-research-assistant
3. Set Up a Virtual Environment (Recommended)
Isolate your dependencies using a Python virtual environment:

Bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
4. Install Dependencies
Install all the underlying required libraries including AutoGen, Streamlit, and environment management tools:

Bash
pip install streamlit pyautogen python-dotenv requests scholarly
5. Configure Environment Variables
Create a file named .env in the root directory of the project to store your secret API key safely:

Code snippet
GROQ_API_KEY=your_actual_groq_api_key_here
6. Run the Application
Boot up the local Streamlit web server by running:

Bash
streamlit run app.py
Once executed, your terminal will confirm initialization, and the dashboard will automatically open in your default web browser at http://localhost:8501.

💡 Usage Guide
Enter a Topic: Open the dashboard and input any academic domain, theory, or keyword (e.g., "Retrieval-Augmented Generation", "Quantum Computing Architecture", or "Graph Neural Networks").

Search and Analyze: Click the Search & Analyze button.

Review Results: The application will load the top matching papers. Under each paper title, explore the Concise Summary and Pros & Cons Analysis tabs compiled in real-time by your autonomous AI research team.

🛡️ License
This project is open-source and available under the MIT License.