from workflow.pipelines.steps.base_step import BaseStep
from workflow.pipelines.category_loop import CategoryLoopEngine


class CategoryLoopStep(BaseStep):
    name = "category_loop"

    def __init__(
        self,
        loop_engine: CategoryLoopEngine | None = None,
    ):
        self.loop_engine = loop_engine or CategoryLoopEngine()

    def run(self, context: dict) -> dict:
        """
        Richiede:
            context["title"]
            context["themes"]
            context["summary"]

        Aggiunge:
            context["category_final"]
            context["category_score"]
            context["category_attempts"]
            context["category_excluded_previous"]
            context["category_loop_success"]
        """

        title = context.get("title", "")
        themes = context.get("themes", [])
        summary = context.get("summary", "")

        result = self.loop_engine.run(
            title=title,
            themes=themes,
            summary=summary
        )

        # Aggiorna contesto con tutte le info prodotte dal loop
        context["category_final"] = result.get("category")
        context["category_score"] = result.get("score")
        context["category_attempts"] = result.get("attempts")
        context["category_excluded_previous"] = result.get("excluded_category")
        context["category_loop_success"] = result.get("success", False)

        return context
