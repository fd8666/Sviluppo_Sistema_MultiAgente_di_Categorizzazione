from workflow.services.api.event_fetcher import EventFetcher


def test_fetch_events():
    fetcher = EventFetcher()

    print("\nFETCHING FIRST PAGE...\n")
    events = fetcher.fetch_events_from_page(page=1)

    print(f"NUMERO EVENTI COMPLETI RICEVUTI: {len(events)}")

    # Stampiamo 3 eventi completi
    for idx, event in enumerate(events[:3], start=1):
        body = event.get("body", {})

        print("\n==================== EVENTO", idx, "====================")

        print("ID:", body.get("id"))
        print("SLUG:", body.get("slug"))
        print("TITLE:", body.get("title"))

        print("\n--- DESCRIZIONE COMPLETA (HTML) ---")
        print(body.get("content", ""))  # HTML completo del contenuto evento

        print("====================================================\n")


def run_all():
    test_fetch_events()


if __name__ == "__main__":
    run_all()
