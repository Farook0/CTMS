# agents/project_manager.py
from crewai import Agent
from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY, GROQ_MODEL

def create_project_manager_agent(llm):
    return Agent(
        role="Project Manager",
        goal="Coordinate task allocation and track project progress",
        backstory="An experienced project manager who excels in breaking down complex projects and assigning tasks efficiently",
        verbose=True,
        llm=llm,
        allow_delegation=True
    )