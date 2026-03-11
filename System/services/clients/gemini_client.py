from workflow.config.settings import settings
from datapizza.clients.google import GoogleClient

client_gemini_2_5_flash = GoogleClient(
    api_key = settings.GOOGLE_API_KEY,
    model = settings.DEFAULT_MODEL, 
    temperature = settings.TEMPERATURE
    )