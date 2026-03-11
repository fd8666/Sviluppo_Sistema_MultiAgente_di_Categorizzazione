# workflow/test/flows/test_full_batch_5.py

from workflow.services.api.base_fetcher import CSVEventFetcher
from workflow.pipelines.single_event_categpry_loop_flow import build_event_category_loop_pipeline
from workflow.database.event_saver import EventSaver
from workflow.database.db import init_db
import time


def test_batch_5():
    print("\n=== TEST BATCH (5 EVENTI) ===")

    init_db()
    saver = EventSaver()

    csv_path = "workflow/data/event_static_100_tests.csv"
    fetcher = CSVEventFetcher(csv_path)

    pipeline = build_event_category_loop_pipeline()

    events = fetcher.fetch_first(5)

    results = []
    for i, event_raw in enumerate(events, start=1):
        print(f"\n--- PROCESSING EVENT {i}/5 ---")

        start = time.time()
        result = pipeline.run(event_raw)
        end = time.time()

        # salva
        saver.save(result)
        results.append(result)

        print(f"TIME: {round(end - start, 2)} sec")
        print(f"ID: {result.get('id')}")
        print(f"Title: {result.get('title')}")
        print(f"Summary OK: {result.get('summary') is not None}")
        print(f"Themes OK: {result.get('themes') is not None}")
        print(f"Final Category: {result.get('category_final')}")
        print(f"Errors: {result.get('errors')}")

    print("\n=== END TEST (5 EVENTI) ===")


if __name__ == "__main__":
    test_batch_5()
