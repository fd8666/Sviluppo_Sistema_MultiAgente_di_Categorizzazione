from workflow.services.clients.gemini_client import client_gemini_2_5_flash
from workflow.config.settings import settings
from workflow.services.throttler import Throttler

class SummaryAgent:

    def __init__(self, model_client=client_gemini_2_5_flash, throttler = None):

        self.client = model_client
        self.prompt_template = settings.PROMPTS["summary"]
        self.system_message = settings.ROLES["summary"]
        self.throttler = throttler or Throttler(5.0) 

    def run(self, title : str, description : str) -> str:
        
        prompt = self.prompt_template.format(
            title = title,
            content = description
        )

        self.throttler.wait()
        
        response = self.client.invoke(
            input= prompt,
            system_prompt= self.system_message,
        )

        return response.text
