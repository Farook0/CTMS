# main.py
import os
from crewai import Crew, Task, Process
from langchain_groq import ChatGroq

from config.settings import GROQ_API_KEY, GROQ_MODEL
from database.manager import DatabaseManager
from agents.project_manager import create_project_manager_agent
from agents.task_allocator import create_task_allocator_agent
from agents.progress_tracker import create_progress_tracker_agent

class CollaborativeTaskManagementSystem:
    def __init__(self):
        # Initialize Groq Language Model
        self.llm = ChatGroq(
            temperature=0.7,
            model_name=GROQ_MODEL,
            groq_api_key=GROQ_API_KEY
        )
        
        # Initialize Database
        self.db_manager = DatabaseManager()
        
        # Create Agents
        self.project_manager = create_project_manager_agent(self.llm)
        self.task_allocator = create_task_allocator_agent(self.llm)
        self.progress_tracker = create_progress_tracker_agent(self.llm)

    def create_project_tasks(self):
        # Create Project
        project = self.db_manager.create_project(
            "CrewAI Task Management", 
            "Collaborative project management system"
        )

        # Task Creation Task
        create_project_task = Task(
            description=f"Break down project {project.name} into detailed, manageable tasks. Define scope, milestones, and initial task list.",
            agent=self.project_manager,
            expected_output="Comprehensive project breakdown with tasks, priorities, and estimated timelines"
        )

        # Task Allocation Task
        allocate_tasks_task = Task(
            description="Assign tasks to team members based on their skills, availability, and current workload.",
            agent=self.task_allocator,
            expected_output="Task assignment matrix with team member allocations and task details"
        )

        # Progress Monitoring Task
        track_progress_task = Task(
            description="Create a real-time progress tracking mechanism to monitor task completion and identify potential bottlenecks.",
            agent=self.progress_tracker,
            expected_output="Progress report with task status, completion percentage, and recommendations"
        )

        return [create_project_task, allocate_tasks_task, track_progress_task]

    def run_workflow(self):
        # Create Users (Demo Purpose)
        user1 = self.db_manager.create_user('johndoe', 'john@example.com', 'Developer')
        user2 = self.db_manager.create_user('janedoe', 'jane@example.com', 'Designer')

        # Initialize Crew with Sequential Process
        crew = Crew(
            agents=[
                self.project_manager, 
                self.task_allocator, 
                self.progress_tracker
            ],
            tasks=self.create_project_tasks(),
            verbose=2,
            process=Process.sequential
        )

        # Execute the workflow
        result = crew.kickoff()
        return result

def main():
    task_management_system = CollaborativeTaskManagementSystem()
    workflow_results = task_management_system.run_workflow()
    print("Workflow Completed. Results:", workflow_results)

if __name__ == "__main__":
    main()