from workflow.services.clients.gemini_client import client_gemini_2_5_flash
from workflow.model.scheme import ThemesOutput
from workflow.config.settings import settings
from workflow.services.throttler import Throttler

class ThemesAgent:

    def __init__(self, model_client=client_gemini_2_5_flash, throttler = None):
        self.client = model_client
        self.prompt_template = settings.PROMPTS["themes"]
        self.system_message = settings.ROLES["themes"]
        self.throttler = throttler or Throttler(5.0)

    def run(self, title : str, description : str):
        prompt = self.prompt_template.format(
            title=title,
            content=description
        )

        self.throttler.wait()

        response = self.client.structured_response(
            input= prompt,
            system_prompt= self.system_message,
            output_cls= ThemesOutput
        )

        return  response.structured_data[0].tags