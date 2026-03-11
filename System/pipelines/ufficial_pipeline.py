from workflow.services.api.base_fetcher import CSVEventFetcher
from workflow.pipelines.single_event_categpry_loop_flow import build_event_category_loop_pipeline
from workflow.database.event_saver import EventSaver


class FinalBatchPipeline:

    def __init__(self, csv_path: str, processor=None, saver=None):
        self.fetcher = CSVEventFetcher(csv_path)
        self.processor = processor or build_event_category_loop_pipeline()
        self.saver = saver or EventSaver()

    def run(self, limit: int = 100):
        events = self.fetcher.fetch_first(limit)

        print(f"\n=== START FINAL BATCH (processing {len(events)} events) ===")

        for i, event in enumerate(events, start=1):
            print(f"\n--- PROCESSING EVENT {i}/{len(events)} ---")
            result = self.processor.run(event)
            self.saver.save(result)

        print("\n=== END FINAL BATCH ===")
