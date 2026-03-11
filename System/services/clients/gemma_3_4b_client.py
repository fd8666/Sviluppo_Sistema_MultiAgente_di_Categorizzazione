from datapizza.clients.openai_like import OpenAILikeClient
from workflow.config.settings import settings

client_gemma_3_4b = OpenAILikeClient(
    api_key="",
    model="gemma3:4b",
    base_url="http://localhost:11434/v1",
    temperature=settings.TEMPERATURE
)

