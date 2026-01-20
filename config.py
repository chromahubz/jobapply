import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration settings for the job application assistant"""

    # API Keys
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    # Personal Information
    YOUR_NAME = os.getenv("YOUR_NAME", "")
    YOUR_EMAIL = os.getenv("YOUR_EMAIL", "")
    YOUR_PHONE = os.getenv("YOUR_PHONE", "")
    YOUR_LINKEDIN = os.getenv("YOUR_LINKEDIN", "")

    # Resume/CV path
    RESUME_PATH = os.getenv("RESUME_PATH", "./resume.txt")

    # LLM Settings
    LLM_MODEL = "llama-3.3-70b-versatile"  # Groq model
    LLM_TEMPERATURE = 0.7
    LLM_MAX_TOKENS = 2000

    # Output directory
    OUTPUT_DIR = Path("./applications")

    @classmethod
    def validate(cls):
        """Validate required configuration"""
        if not cls.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is required. Please set it in .env file")

        # Create output directory if it doesn't exist
        cls.OUTPUT_DIR.mkdir(exist_ok=True)

    @classmethod
    def load_resume(cls):
        """Load resume text from file"""
        resume_path = Path(cls.RESUME_PATH)
        if resume_path.exists():
            return resume_path.read_text(encoding='utf-8')
        return ""
