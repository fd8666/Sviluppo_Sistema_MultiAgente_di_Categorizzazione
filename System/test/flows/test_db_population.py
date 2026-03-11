from workflow.database.db import init_db
from workflow.database.event_saver import EventSaver
from workflow.services.api.event_fetcher import EventFetcher
from workflow.pipelines.single_event_categpry_loop_flow import build_event_category_loop_pipeline


def test_db_population():
    print("\n=== START DB POPULATION TEST ===\n")

    # 1) Inizializza il DB
    init_db()
    saver = EventSaver()

    # 2) Fetcher + pipeline
    fetcher = EventFetcher()
    pipeline = build_event_category_loop_pipeline()

    print("Fetching 3 events from API...\n")
    events = fetcher.fetch_events_from_page(1)[:3]

    for i, event_raw in enumerate(events, start=1):
        print(f"--- PROCESSING EVENT {i} ---")

        context = pipeline.run(event_raw)

        # 3) Salvataggio nel DB
        saver.save(context)

        print("Saved to DB:", context.get("id"), context.get("title"))
        print()

    print("=== END DB POPULATION TEST ===")


if __name__ == "__main__":
     test_db_population()
