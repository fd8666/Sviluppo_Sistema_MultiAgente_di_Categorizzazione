from typing import List, Callable

from workflow.pipelines.single_event_categpry_loop_flow import build_event_category_loop_pipeline
from workflow.services.api.event_fetcher import EventFetcher


class MultiEventPipeline:
    """
    Pipeline che gestisce un'intera pagina di eventi provenienti da una sorgente (API o DB).
    Esegue:
    - fetch eventi
    - pipeline per evento singolo
    - salvataggio risultati
    """

    def __init__(self, fetcher, single_pipeline, save_fn: Callable[[dict], None] | None = None):
        """
        fetcher: oggetto che fornisce una funzione fetch_events_from_page(page)
        single_pipeline: pipeline per un singolo evento
        save_fn: funzione facoltativa per salvare il risultato nel DB
        """
        self.fetcher = fetcher
        self.single_pipeline = single_pipeline
        self.save_fn = save_fn

    def run(self, page: int = 1) -> List[dict]:
        """
        Restituisce tutti i risultati della pagina.
        """
        print(f"\n=== FETCHING EVENTS PAGE {page} ===")
        events = self.fetcher.fetch_events_from_page(page)
        results = []

        for idx, event_raw in enumerate(events, start=1):
            print(f"\n--- PROCESSING EVENT {idx}/{len(events)} ---\n")
            result = self.single_pipeline.run(event_raw)

            # salvataggio opzionale
            if self.save_fn:
                self.save_fn(result)

            results.append(result)

        return results
    
def build_multi_event_flow(fetcher=None, save_fn=None, throttler=None):

    if fetcher is None:
        fetcher = EventFetcher()

    single_pipeline = build_event_category_loop_pipeline(throttler=throttler)

    return MultiEventPipeline(fetcher, single_pipeline, save_fn)
