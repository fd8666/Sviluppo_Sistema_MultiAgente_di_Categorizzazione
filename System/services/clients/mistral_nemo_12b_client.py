from datapizza.clients.openai_like import OpenAILikeClient
from workflow.config.settings import settings

client_mistral_nemo_12b = OpenAILikeClient(
    api_key="",
    model="mistral-nemo:12b",
    base_url="http://localhost:11434/v1",
    temperature=settings.TEMPERATURE
)
