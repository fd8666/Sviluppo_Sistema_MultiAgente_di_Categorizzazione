import time
from workflow.services.api.base_fetcher import CSVEventFetcher
from workflow.pipelines.local_model_example import build_event_category_loop_pipeline_local

# ANSI colors
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"


def print_section(title: str):
    print(f"\n{CYAN}{'='*80}\n{title}\n{'='*80}{RESET}")


def print_entry(key, value, color=RESET):
    print(f"{color}{key}: {RESET}{value}")


def test_local_pipeline(n: int = 3):
    print_section("TEST PIPELINE LOCALE (llama 3.2 3B per Summary + Themes)")

    fetcher = CSVEventFetcher("workflow/data/event_static_100_tests.csv")
    pipeline = build_event_category_loop_pipeline_local()

    events = fetcher.fetch_first(n)

    for i, event in enumerate(events, start=1):
        print_section(f"EVENTO {i}/{n}")

        start = time.time()
        result = pipeline.run(event)
        end = time.time()

        # --- stampa risultati ---
        print_entry("ID", result.get("id"), GREEN)
        print_entry("Titolo", result.get("title"))
        print_entry("Slug", result.get("slug"))
        print_entry("Description (preview)", result.get("description")[:180] + "...")

        print_entry("Summary", result.get("summary"), YELLOW)
        print_entry("Themes", ", ".join(result.get("themes", [])), YELLOW)

        print_entry("Final Category", result.get("category_final"), GREEN)
        print_entry("Score", result.get("category_score"), GREEN)
        print_entry("Attempts", result.get("category_attempts"))
        print_entry("Excluded previous", result.get("category_excluded_previous"))

        print_entry("Loop success", result.get("category_loop_success"), GREEN if result.get("category_loop_success") else RED)

        if result.get("errors"):
            print_entry("Errors", result.get("errors"), RED)

        print(f"\n⏱️ Tempo impiegato: {round(end - start, 2)} secondi\n")


if __name__ == "__main__":
    test_local_pipeline(3)
