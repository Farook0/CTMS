# agents/task_allocator.py
from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY, GROQ_MODEL
from crewai import Agent
def create_task_allocator_agent(llm):
    return Agent(
        role="Task Allocation Specialist",
        goal="Assign tasks to team members based on skills and workload",
        backstory="A strategic resource allocation expert who optimizes team productivity",
        verbose=True,
        llm=llm,
        allow_delegation=True
    )