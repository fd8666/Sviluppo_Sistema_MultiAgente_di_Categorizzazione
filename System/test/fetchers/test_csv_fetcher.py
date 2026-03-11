from workflow.services.api.base_fetcher import CSVEventFetcher

def test_csv_fetcher():
    print("\n=== TEST CSV FETCHER ===")

    fetcher = CSVEventFetcher("workflow/data/event_static_100_tests.csv")
    events = fetcher.fetch_first(3)

    print("Totale eventi caricati:", len(fetcher.fetch_all()))

    for i, ev in enumerate(events, start=1):
        print(f"\n--- EVENTO {i} ---")
        print("ID:", ev["id"])
        print("Titolo:", ev["title"])
        print("Descrizione:\n", ev["description"])
        
if __name__ == "__main__":
    test_csv_fetcher()
