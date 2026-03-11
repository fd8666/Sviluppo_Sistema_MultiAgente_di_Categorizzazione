from workflow.services.api.event_fetcher import EventFetcher
from workflow.pipelines.single_event_flow import build_default_single_event_pipeline


def test_single_event_pipeline():
    fetcher = EventFetcher()
    pipeline = build_default_single_event_pipeline()

    print("\nFETCHING RAW EVENT FROM API...\n")
    events = fetcher.fetch_events_from_page(page=1)
    event_raw = events[0]

    result = pipeline.run(event_raw)

    print("\n=== PIPELINE RESULT ===")
    print("ID:", result.get("id"))
    print("Title:", result.get("title"))
    print("Slug:", result.get("slug"))
    print("\nDescription:\n", result.get("description"))

    print("\nSummary:\n", result.get("summary"))
    print("\nThemes:", result.get("themes"))
    print("\nCategory assigned:", result.get("category_assigned"))
    print("Evaluation score:", result.get("evaluation_score"))

    print("\nErrors:", result.get("errors"))


if __name__ == "__main__":
    test_single_event_pipeline()
