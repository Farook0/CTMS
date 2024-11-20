from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY,GROQ_MODEL
from crewai import Agent
def create_progress_tracker_agent(llm):
    return Agent(
        role="Progress Tracker",
        goal="Monitor task completion and provide real-time status updates",
        backstory="A detail-oriented analyst who ensures project milestones are met",
        verbose=True,
        llm=llm,
        allow_delegation=True
    )