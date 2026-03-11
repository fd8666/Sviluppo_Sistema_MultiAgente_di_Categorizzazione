from workflow.agents.category_agent import CategoryAgent
from workflow.agents.evaluator_agent import EvaluatorAgent
from workflow.services.throttler import Throttler

class CategoryLoopEngine:

    def __init__(
        self,
        category_agent: CategoryAgent | None = None,
        evaluator_agent: EvaluatorAgent | None = None,
        min_confidence: int = 85,
        max_attempts: int = 5,
        throttler = None
    ):
        
        self.category_agent = category_agent or CategoryAgent()
        self.evaluator_agent = evaluator_agent or EvaluatorAgent()
        self.min_confidence = min_confidence
        self.max_attempts = max_attempts
        self.throttler = throttler or Throttler(5.0)

    def run( self, title: str, themes: list[str], summary: str):

        excluded_category: str | None = None
        attempts = 0


        while attempts < self.max_attempts:
            
            attempts += 1

            self.throttler.wait()

            category = self.category_agent.run(

                title= title,
                short_description= summary,
                themes= themes,
                blacklist= excluded_category

            )

            self.throttler.wait()
            
            # 2. Valutazione
            score = self.evaluator_agent.run(
                title=title,
                themes=themes,
                summary=summary,
                assigned_category=category
            )

            # 3. Se score buono → finito
            if score >= self.min_confidence:
                return {
                    
                    "category": category,
                    "score": score,
                    "attempts": attempts,
                    "excluded_category": excluded_category,
                    "success": True,

                }

            # prossimo giro: escludo SOLO la categoria appena tentata
            excluded_category = category
        
        # fallback finale
        return {

            "category": "N/A",
            "score": 50,
            "attempts": attempts,
            "excluded_category": excluded_category,
            "success": False,
            "fallback": True,

        }