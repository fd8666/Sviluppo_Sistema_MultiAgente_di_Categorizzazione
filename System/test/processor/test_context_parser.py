from workflow.services.api.event_fetcher import EventFetcher
from workflow.services.processor.context_parser import ContextParser


def test_context_parser():
    fetcher = EventFetcher()
    parser = ContextParser()

    print("\nFETCHING RAW EVENT...\n")
    events = fetcher.fetch_events_from_page(page=1)
    event_raw = events[0]

    dto = parser.parse(event_raw)

    print("\n=== EVENT DTO ===")
    print("ID:", dto["id"])
    print("Titolo:", dto["title"])
    print("Slug:", dto["slug"])
    print("\nDescrizione (clean):\n", dto["description"])


if __name__ == "__main__":
    test_context_parser()
