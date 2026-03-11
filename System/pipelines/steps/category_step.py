from workflow.pipelines.steps.base_step import BaseStep
from workflow.agents.category_agent import CategoryAgent


class CategoryStep(BaseStep):
    name = "category"

    def __init__(self, agent: CategoryAgent | None = None, throttler=None):
        self.agent = agent or CategoryAgent(throttler=throttler)

    def run(self, context: dict) -> dict:
        """
        Richiede:
            context["title"]
            context["themes"]
            context["summary"]
        Aggiunge:
            context["category_assigned"] (stringa)
        """
        title = context.get("title", "")
        themes = context.get("themes", [])
        summary = context.get("summary", "")

        category = self.agent.run(title, themes, summary)
        context["category_assigned"] = category

        return context
