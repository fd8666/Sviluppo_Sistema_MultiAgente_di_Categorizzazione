from typing import List

from workflow.pipelines.steps.base_step import BaseStep
from workflow.pipelines.steps.context_step import ContextParserStep
from workflow.pipelines.steps.summary_step import SummaryStep
from workflow.pipelines.steps.themes_step import ThemesStep
from workflow.pipelines.steps.category_loop_step import CategoryLoopStep

from workflow.agents.summary_agent import SummaryAgent
from workflow.agents.themes_agent import ThemesAgent

from workflow.services.throttler import Throttler

from workflow.services.clients.llama_3b_client import client_llama_3b

class EventCategoryLoopPipeline:
    """
    Pipeline completa e robusta per la classificazione degli eventi.
    Summary + Themes = local model (Gemma 3 4B)
    Category Loop = Gemini
    """

    def __init__(self, steps: List[BaseStep]):
        self.steps = steps

    def run(self, event_raw: dict) -> dict:
        context: dict = {"event_raw": event_raw, "errors": {}}

        for step in self.steps:
            try:
                context = step.run(context)
            except Exception as e:
                context["errors"][step.name] = str(e)

        return context


def build_event_category_loop_pipeline_local(throttler=None) -> EventCategoryLoopPipeline:
    """
    Pipeline che usa modelli locali SOLO per:
        - Summary
        - Themes
    """

    throttler = throttler or Throttler(1.0)  # throttler molto più rapido per modelli locali

    steps = [
        ContextParserStep(),
        SummaryStep(
            agent=SummaryAgent(model_client=client_llama_3b),
            throttler=throttler,
        ),
        ThemesStep(
            agent=ThemesAgent(model_client=client_llama_3b),
            throttler=throttler,
        ),
        CategoryLoopStep(),  # continua a usare Gemini
    ]

    return EventCategoryLoopPipeline(steps)
