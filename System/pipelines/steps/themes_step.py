from workflow.pipelines.steps.base_step import BaseStep
from workflow.agents.themes_agent import ThemesAgent


class ThemesStep(BaseStep):
    name = "themes"

    def __init__(self, agent: ThemesAgent | None = None, throttler=None):
        self.agent = agent or ThemesAgent(throttler=throttler)

    def run(self, context: dict) -> dict:
        """
        Richiede:
            context["title"]
            context["description"]
        Aggiunge:
            context["themes"] -> List[str]
        """
        title = context.get("title", "")
        description = context.get("description", "")

        themes = self.agent.run(title, description)
        context["themes"] = themes

        return context
