from workflow.services.api.event_fetcher import EventFetcher
from workflow.pipelines.single_event_categpry_loop_flow import build_event_category_loop_pipeline


def test_full_pipeline_3_events():

    print("\n=== FULL PIPELINE TEST (3 events) ===")

    fetcher = EventFetcher()
    pipeline = build_event_category_loop_pipeline()

    print("\nFetching events from API page 1...\n")
    events = fetcher.fetch_events_from_page(page=4)

    # ▶️ Limit to 3 events
    events = events[:3]

    results = []

    for idx, event_raw in enumerate(events, start=1):
        print(f"\n--- PROCESSING EVENT {idx}/3 ---")

        result = pipeline.run(event_raw)
        results.append(result)

        # Pretty printing results
        print("ID:", result.get("id"))
        print("Title:", result.get("title"))
        print("Slug:", result.get("slug"))
        print("\nSummary:\n", result.get("summary"))
        print("\nThemes:", result.get("themes"))
        print("\nFinal Category:", result.get("category_final"))
        print("Score:", result.get("category_score"))
        print("Attempts:", result.get("category_attempts"))
        print("Excluded category:", result.get("category_excluded"))
        print("Loop success:", result.get("category_loop_success"))
        print("\nErrors:", result.get("errors"))
        print("\n------------------------------")

    print("\n=== END FULL PIPELINE TEST ===")


if __name__ == "__main__":
    test_full_pipeline_3_events()
