from workflow.services.api.event_fetcher import EventFetcher
from workflow.pipelines.single_event_categpry_loop_flow import build_event_category_loop_pipeline


def test_robust_event_pipeline():
    fetcher = EventFetcher()
    pipeline = build_event_category_loop_pipeline()

    print("\nFETCHING RAW EVENT FROM API...\n")
    events = fetcher.fetch_events_from_page(page=2)
    event_raw = events[0]

    result = pipeline.run(event_raw)

    print("\n=== ROBUST EVENT PIPELINE RESULT ===")
    print("ID:", result.get("id"))
    print("Title:", result.get("title"))
    print("Slug:", result.get("slug"))
    print("\nDescription:\n", result.get("description"))

    print("\nSummary:\n", result.get("summary"))
    print("\nThemes:", result.get("themes"))

    print("\nFinal Category:", result.get("category_final"))
    print("Confidence Score:", result.get("category_score"))
    print("Attempts:", result.get("category_attempts"))
    print("Excluded category:", result.get("category_excluded_previous"))
    print("Success:", result.get("category_loop_success"))

    print("\nErrors:", result.get("errors"))


if __name__ == "__main__":
    test_robust_event_pipeline()
