from workflow.pipelines.steps.base_step import BaseStep
from workflow.agents.summary_agent import SummaryAgent


class SummaryStep(BaseStep):
    name = "summary"

    def __init__(self, agent: SummaryAgent | None = None, throttler=None):
        self.agent = agent or SummaryAgent(throttler=throttler)

    def run(self, context: dict) -> dict:
        """
        Richiede:
            context["title"]
            context["description"]
        Aggiunge:
            context["summary"]
        """
        title = context.get("title", "")
        description = context.get("description", "")

        summary = self.agent.run(title, description)
        context["summary"] = summary

        return context
