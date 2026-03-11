import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

# CARICO IL .env ESPPLICITAMENTE DA config/
load_dotenv(BASE_DIR / ".env")

def load_text(relative_path: str) -> str:
    """Legge un file di testo dalla directory config/"""
    full_path = BASE_DIR / relative_path
    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()
    
class Settings:

    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
    DEFAULT_MODEL: str = os.getenv("DEFAULT_MODEL", "gemini-2.0-flash")
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.2"))

    API_BASE_URL: str = os.getenv("API_BASE_URL", "")

    PROMPTS = {
        "summary": load_text("prompts/summary_prompt.md"),
        "themes": load_text("prompts/themes_prompt.md"),
        "category": load_text("prompts/category_prompt.md"),
        "evaluator": load_text("prompts/evaluator_prompt.md"),
    }

    ROLES = {
        "summary": load_text("roles/summary_role.md"),
        "themes": load_text("roles/themes_role.md"),
        "category": load_text("roles/category_role.md"),
        "evaluator": load_text("roles/evaluator_role.md"),
    }

    DB_URL: str = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{(BASE_DIR.parent / 'events.db')}"
    )

settings = Settings()
