import csv

class CSVEventFetcher:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.events = self._load_events()

    def _load_events(self) -> list[dict]:
        events = []

        with open(self.csv_path, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)

            for row in reader:
                event_id = row.get("IdEvento")
                title = row.get("Titolo", "")
                description = row.get("Descrizione", "")

                events.append({
                    "id": int(event_id) if event_id else None,
                    "slug": None,  # non esiste nel CSV
                    "title": title,
                    "description": description,
                })

        return events

    # restituisce tutti gli eventi
    def fetch_all(self) -> list[dict]:
        return self.events

    # restituisce i primi n
    def fetch_first(self, n: int) -> list[dict]:
        return self.events[:n]

    # simula fetch per pagina
    def fetch_page(self, page: int = 1, page_size: int = 25) -> list[dict]:
        start = (page - 1) * page_size
        end = start + page_size
        return self.events[start:end]
