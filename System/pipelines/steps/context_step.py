from workflow.services.processor.context_parser import ContextParser
from workflow.pipelines.steps.base_step import BaseStep

class ContextParserStep(BaseStep):
    name = "context_parser"

    def __init__(self, parser: ContextParser | None = None):
        self.parser = parser or ContextParser()

    def run(self, context: dict) -> dict:
        """
        Si aspetta:
            context["event_raw"]
        Aggiunge:
            id, title, slug, description
        """
        event_raw = context.get("event_raw")
        if event_raw is None:
            raise ValueError("Missing 'event_raw' in context.")

        dto = self.parser.parse(event_raw)

        context.update(dto)  # aggiunge id, title, slug, description
        return context