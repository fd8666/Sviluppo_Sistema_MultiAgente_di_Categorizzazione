from workflow.pipelines.steps.base_step import BaseStep
from workflow.agents.evaluator_agent import EvaluatorAgent


class EvaluatorStep(BaseStep):
    name = "evaluator"

    def __init__(self, agent: EvaluatorAgent | None = None, throttler=None):
        self.agent = agent or EvaluatorAgent(throttler=throttler)

    def run(self, context: dict) -> dict:
        """
        Richiede:
            context["title"]
            context["themes"]
            context["summary"]
            context["category_assigned"]
        Aggiunge:
            context["evaluation_score"] (int)
        """
        title = context.get("title", "")
        themes = context.get("themes", [])
        summary = context.get("summary", "")
        category = context.get("category_assigned", "")

        score = self.agent.run(title, themes, summary, category)
        context["evaluation_score"] = score

        return context
