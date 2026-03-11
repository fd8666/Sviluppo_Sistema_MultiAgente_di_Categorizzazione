from datapizza.tracing import ContextTracing

from workflow.database.init_db import init_db
from workflow.services.api.base_fetcher import CSVEventFetcher
from workflow.pipelines.single_event_categpry_loop_flow import build_event_category_loop_pipeline
from workflow.database.event_saver import EventSaver


def test_trace_print_5():
    print("\n=== TEST TRACE PRINT (5 EVENTI) ===")

    init_db()

    fetcher = CSVEventFetcher("workflow/data/event_static_100_tests.csv")
    pipeline = build_event_category_loop_pipeline()
    saver = EventSaver()

    events = fetcher.fetch_first(5)

    for i, ev in enumerate(events, start=1):
        ev_id = ev.get("id")

        # Il Trace Summary lo stampa già Datapizza in automatico
        with ContextTracing().trace(f"event_{i}_{ev_id}"):
            result = pipeline.run(ev)

        saver.save(result)
        print(f"[{i}/5] ok event_id={ev_id} title={result.get('title')}")

    print("DONE.")


if __name__ == "__main__":
    test_trace_print_5()
