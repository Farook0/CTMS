# database/manager.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, User, Project, Task, TaskStatus
from config.settings import DATABASE_URL

class DatabaseManager:
    def __init__(self, db_url=DATABASE_URL):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
    
    def create_user(self, username, email, role):
        session = self.Session()
        new_user = User(username=username, email=email, role=role)
        session.add(new_user)
        session.commit()
        session.close()
        return new_user
    
    def create_project(self, name, description):
        session = self.Session()
        new_project = Project(name=name, description=description)
        session.add(new_project)
        session.commit()
        session.close()
        return new_project
    
    def create_task(self, title, description, project_id, assignee_id, 
                    status=TaskStatus.NOT_STARTED, priority=3):
        session = self.Session()
        new_task = Task(
            title=title, 
            description=description, 
            project_id=project_id, 
            assignee_id=assignee_id,
            status=status,
            priority=priority
        )
        session.add(new_task)
        session.commit()
        session.close()
        return new_task
    
    def get_user_tasks(self, user_id):
        session = self.Session()
        tasks = session.query(Task).filter(Task.assignee_id == user_id).all()
        session.close()
        return tasks
    
    def update_task_status(self, task_id, new_status):
        session = self.Session()
        task = session.query(Task).filter(Task.id == task_id).first()
        if task:
            task.status = new_status
            session.commit()
        session.close()
        return task