from workflow.services.clients.gemini_client import client_gemini_2_5_flash
from workflow.config.settings import settings
from workflow.model.scheme import EvaluatorOutput
from workflow.services.throttler import Throttler


class EvaluatorAgent:

    def __init__(self, model_client=client_gemini_2_5_flash, throttler = None):
        self.client = model_client
        self.prompt_template = settings.PROMPTS["evaluator"]
        self.system_message = settings.ROLES["evaluator"]
        self.throttler = throttler or Throttler(5.0)


    def run(self, title: str, themes: list[str], summary: str, assigned_category: str) -> int:
        
        self.throttler.wait()

        prompt = self.prompt_template.format(
            title=title,
            themes=", ".join(themes),
            summary=summary,
            assigned_category=assigned_category
        )

        response = self.client.structured_response(
            input=prompt,
            system_prompt=self.system_message,
            output_cls=EvaluatorOutput
        )

        result: EvaluatorOutput = response.structured_data[0]
        return result.confidence
