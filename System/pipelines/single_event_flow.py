from typing import List

from workflow.pipelines.steps.base_step import BaseStep
from workflow.pipelines.steps.context_step import ContextParserStep
from workflow.pipelines.steps.summary_step import SummaryStep
from workflow.pipelines.steps.themes_step import ThemesStep
from workflow.pipelines.steps.category_step import CategoryStep
from workflow.pipelines.steps.evaluator_step import EvaluatorStep


class SingleEventPipeline:
    """
    Pipeline per processare un singolo evento:
        raw_event -> parser -> summary -> themes -> category -> evaluator
    """

    def __init__(self, steps: List[BaseStep]):
        self.steps = steps

    def run(self, event_raw: dict) -> dict:
        # context iniziale
        context: dict = {
            "event_raw": event_raw,
            "errors": {}
        }

        for step in self.steps:
            try:
                context = step.run(context)
            except Exception as e:
                # registriamo l'errore ma NON fermiamo la pipeline
                context["errors"][step.name] = str(e)

        return context


def build_default_single_event_pipeline() -> SingleEventPipeline:
    """
    Costruisce la pipeline con gli step di default e agent di default.
    """
    steps: List[BaseStep] = [
        ContextParserStep(),
        SummaryStep(),
        ThemesStep(),
        CategoryStep(),
        EvaluatorStep(),
    ]
    return SingleEventPipeline(steps=steps)
