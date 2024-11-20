# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

# Database Configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///task_management.db')

# Groq Configuration
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
GROQ_MODEL = os.getenv('GROQ_MODEL', 'llama3-70b-8192')

# Application Settings
DEBUG = os.getenv('DEBUG', 'False') == 'True'