from workflow.config.settings import settings
from workflow.services.clients.gemini_client import client_gemini_2_5_flash
from workflow.model.scheme import CategoryOutput
from workflow.services.throttler import Throttler

class CategoryAgent:

    def __init__(self, model_client = client_gemini_2_5_flash, throttler = None):
        
        self.client=model_client
        self.prompt_template = settings.PROMPTS["category"]
        self.system_message = settings.ROLES["category"]
        self.throttler = throttler or Throttler(5.0)


    def run(self, title: str, short_description: str, themes: list[str], blacklist: str | None = None) -> str:

        self.throttler.wait()
        
        prompt = self.prompt_template.format(
            
            title=title,
            themes=", ".join(themes),  # il prompt accetta stringa
            summary=short_description,
            excluded_category=blacklist or "None"

        )

        response = self.client.structured_response(

            input= prompt,
            system_prompt= self.system_message,
            output_cls= CategoryOutput

        )

        result: CategoryOutput = response.structured_data[0]
        return result.category.value 