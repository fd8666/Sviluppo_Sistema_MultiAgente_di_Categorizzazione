from typing import List, Optional

from workflow.services.api.event_fetcher import EventFetcher
from workflow.pipelines.single_event_categpry_loop_flow import build_event_category_loop_pipeline
from workflow.database.event_saver import EventSaver
from workflow.services.throttler import Throttler


class BatchManager:
    """
    Gestore batch:
    - prende eventi da EventFetcher
    - esegue la pipeline per ogni evento
    - salva nel DB tramite EventSaver
    - usa Throttler per non saturare le quote LLM
    """

    def __init__(
        self,
        fetcher: EventFetcher,
        pipeline,
        saver: EventSaver,
        throttler: Optional[Throttler] = None,
        max_events_per_page: Optional[int] = None,
    ):
        self.fetcher = fetcher
        self.pipeline = pipeline
        self.saver = saver
        self.throttler = throttler
        self.max_events_per_page = max_events_per_page

    def run_pages(self, pages: List[int]) -> None:
        for page in pages:
            print(f"\n=== PROCESSING PAGE {page} ===")

            try:
                events = self.fetcher.fetch_events_from_page(page)
            except Exception as e:
                print(f"[BATCH] Error fetching page {page}: {e}")
                continue

            if self.max_events_per_page:
                events = events[: self.max_events_per_page]

            total = len(events)
            print(f"[BATCH] Found {total} events on page {page}")

            for idx, event_raw in enumerate(events, start=1):
                body = event_raw.get("body", {})
                event_id = body.get("id")
                slug = body.get("slug")

                print(f"\n--- EVENT {idx}/{total} (ID={event_id}, slug={slug}) ---")

                # throttling
                if self.throttler:
                    self.throttler.wait()

                # esecuzione pipeline
                try:
                    context = self.pipeline.run(event_raw)
                except Exception as e:
                    print(f"[BATCH] Error in pipeline for event {event_id}: {e}")
                    context = {
                        "event_raw": event_raw,
                        "id": event_id,
                        "slug": slug,
                        "errors": {"pipeline": str(e)},
                    }

                # salvataggio
                try:
                    self.saver.save(context)
                    print(f"[BATCH] Event {event_id} saved.")
                except Exception as e:
                    print(f"[BATCH] Error saving event {event_id}: {e}")


def build_default_batch_manager(
    min_interval_sec: float = 2.0,
    max_events_per_page: Optional[int] = None,
) -> BatchManager:
    """
    Costruisce un BatchManager con componenti di default:
    - EventFetcher (API)
    - EventCategoryLoopPipeline (parser+summary+themes+category loop)
    - EventSaver (SQLite)
    - Throttler (per evitare rate limit LLM)
    """
    fetcher = EventFetcher()
    pipeline = build_event_category_loop_pipeline()
    saver = EventSaver()
    throttler = Throttler(min_interval_sec=min_interval_sec)

    return BatchManager(
        fetcher=fetcher,
        pipeline=pipeline,
        saver=saver,
        throttler=throttler,
        max_events_per_page=max_events_per_page,
    )
