from typing import List

from workflow.pipelines.steps.base_step import BaseStep
from workflow.pipelines.steps.context_step import ContextParserStep
from workflow.pipelines.steps.summary_step import SummaryStep
from workflow.pipelines.steps.themes_step import ThemesStep
from workflow.pipelines.steps.category_loop_step import CategoryLoopStep


class EventCategoryLoopPipeline:
    """
    Pipeline completa e robusta per la classificazione degli eventi.
    Esegue:
        - Parser HTML
        - Summary extraction
        - Themes extraction
        - Category loop engine (ricategorizzazione con retry + blacklist)
    """

    def __init__(self, steps: List[BaseStep]):
        self.steps = steps

    def run(self, event_raw: dict) -> dict:
        context: dict = {
            "event_raw": event_raw,
            "errors": {}
        }

        for step in self.steps:
            try:
                context = step.run(context)
            except Exception as e:
                context["errors"][step.name] = str(e)

        return context


def build_event_category_loop_pipeline(throttler=None) -> EventCategoryLoopPipeline:


    steps = [
    ContextParserStep(),
    SummaryStep(throttler=throttler),
    ThemesStep(throttler=throttler),
    CategoryLoopStep(),
    ]

    return EventCategoryLoopPipeline(steps)
