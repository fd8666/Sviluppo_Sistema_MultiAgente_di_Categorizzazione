from datapizza.clients.openai_like import OpenAILikeClient
from workflow.config.settings import settings

client_llama_3b = OpenAILikeClient(
    api_key="",
    model="llama3.2:3b",
    base_url="http://localhost:11434/v1",
    temperature=settings.TEMPERATURE
)

