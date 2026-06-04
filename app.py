import streamlit as st
import os
from dotenv import load_dotenv
from agents import ResearchAgents
from data_loader import DataLoader

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(
    page_title="InsightHub | Virtual Research Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_dotenv()

# 2. Custom CSS Injection for Premium Styling
st.markdown("""
    <style>
    .main-title {
        font-size: 2.8rem !important;
        font-weight: 800;
        background: linear-gradient(45deg, #FF4B4B, #1C83E1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        color: #7d8591;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .paper-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1C83E1;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Configuration (Settings Panel)
with st.sidebar:
    st.markdown("## ⚙️ Configuration Panel")
    st.markdown("Customize your multi-agent workflow parameters here.")
    st.divider()
    
    # Model Status Indicator
    st.success("🤖 LLM Engine: Llama-3.3-70b")
    st.info("⚡ Framework: Microsoft AutoGen")
    
    st.divider()
    st.markdown("### 🔍 Search Constraints")
    max_papers = st.slider("Max Papers to Fetch", min_value=1, max_value=5, value=3)
    
    st.divider()
    st.markdown("📝 **System Status:**")
    groq_api_key = os.getenv("GROQ_API_KEY")
    if groq_api_key:
        st.caption("✅ Groq API Key Connected")
    else:
        st.error("❌ Groq API Key Missing")

# Stop application if key is missing
if not groq_api_key:
    st.error("Please set your GROQ_API_KEY in the environment variables or .env file to continue.")
    st.stop()

# 4. Initialize Backend Instances (Cached for speed)
@st.cache_resource
def init_backend():
    return ResearchAgents(groq_api_key), DataLoader()

agents, data_loader = init_backend()

# 5. Main Dashboard Header
st.markdown('<div class="main-title">🎓 InsightHub</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Advanced Multi-Agent Literature Review & Analysis Workspace</div>', unsafe_allow_html=True)

# 6. Hero Search Workspace
st.markdown("### 🛰️ Central Search Hub")
col_input, col_btn = st.columns([4, 1], gap="medium")

with col_input:
    query = st.text_input(
        label="Search Query",
        label_visibility="collapsed",
        placeholder="Enter research topics, methodologies, or keywords (e.g., Attention Mechanisms)..."
    )

with col_btn:
    # Stylized full-width search button
    search_clicked = st.button("🚀 Analyze Topic", use_container_width=True, type="primary")

st.divider()

# 7. Processing & Results Delivery Interaction
if search_clicked:
    if not query.strip():
        st.warning("⚠️ Please provide a valid search topic before executing the agent loop.")
    else:
        # Step 1: Data Gathering Status
        with st.status("📡 Fetching literature datasets...", expanded=True) as status:
            st.write("Connecting to ArXiv data repository...")
            arxiv_papers = data_loader.fetch_arxiv_papers(query)
            
            # Slice results based on the sidebar slider setup
            all_papers = arxiv_papers[:max_papers]
            
            if not all_papers:
                status.update(label="❌ Search Failed!", state="error", expanded=False)
                st.error("Could not retrieve any matching manuscripts. Try redefining your keyword terms.")
            else:
                status.update(label="✅ Compilation Complete! Handing off to AI Agent Team.", state="complete", expanded=False)

        # Proceed to render results grid if papers exist
        if all_papers:
            # Quick Analytical Metrics Dashboard Summary
            st.markdown("### 📊 Workspace Insights")
            metric_col1, metric_col2, metric_col3 = st.columns(3)
            with metric_col1:
                st.metric(label="Papers Discovered", value=f"{len(all_papers)}")
            with metric_col2:
                st.metric(label="Active Agents Orchestrated", value="2")
            with metric_col3:
                st.metric(label="Inference Platform", value="Groq Cloud")
                
            st.markdown("### 📝 Compiled Literature Dossier")
            
            # Loop and cleanly output each paper inside container components
            for i, paper in enumerate(all_papers, 1):
                with st.container(border=True):
                    # Header Row: Title & Link button aligned perfectly
                    title_col, link_col = st.columns([4, 1])
                    with title_col:
                        st.markdown(f"#### 📄 {i}. {paper['title']}")
                    with link_col:
                        st.markdown(f"**[🔗 Open Full PDF]({paper['link']})**")
                    
                    # Agent Processing Overlay Spinner
                    with st.spinner(f"🤖 Orchestrating agents for Analysis Paper {i}..."):
                        summary = agents.summarize_paper(paper['summary'])
                        adv_dis = agents.analyze_advantages_disadvantages(summary)
                    
                    # Modern Tabbed Layout Architecture split cleanly
                    tab_summary, tab_analysis = st.tabs(["📝 Executive Summary", "⚖️ Strengths & Limitations"])
                    
                    with tab_summary:
                        st.markdown("##### Agent Synthesis")
                        st.info(summary)
                        
                    with tab_analysis:
                        st.markdown("##### Methodological Critique")
                        st.write(adv_dis)