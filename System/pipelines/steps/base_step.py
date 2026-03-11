class BaseStep:

    name: str = "base_step"
    def run(self, context: dict) -> dict:
        raise NotImplementedError("Each step must implement the run() method.")