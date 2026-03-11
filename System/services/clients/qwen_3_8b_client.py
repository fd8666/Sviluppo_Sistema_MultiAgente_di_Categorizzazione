from datapizza.clients.openai_like import OpenAILikeClient
from workflow.config.settings import settings

client_qwen_8b = OpenAILikeClient(
    api_key="",
    model="qwen3:8b",
    base_url="http://localhost:11434/v1",
    temperature=settings.TEMPERATURE
)
