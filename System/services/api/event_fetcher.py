import requests
from workflow.config.settings import settings


class EventFetcher:

    def __init__(self, base_url: str | None = None):
        self.base_url = base_url or settings.API_BASE_URL

        # Header richiesti dall'API per accettare la request
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept": "application/json"
        }

    def fetch_page(self, page: int = 1) -> dict:
        url = f"{self.base_url}/search/events?page={page}"
        response = requests.get(url, headers=self.headers, timeout=10)  # FIX
        response.raise_for_status()
        return response.json()

    def fetch_event(self, slug: str, lang: str = "en") -> dict:
        url = f"{self.base_url}/events/{slug}?&lang={lang}"
        response = requests.get(url, headers=self.headers, timeout=10)  # FIX
        response.raise_for_status()
        return response.json()

    def fetch_events_from_page(self, page: int = 1) -> list[dict]:
        page_data = self.fetch_page(page)
        results = page_data.get("results", [])
        slugs = [event.get("slug") for event in results if event.get("slug")]

        full_events = []
        for slug in slugs:
            full_events.append(self.fetch_event(slug))

        return full_events
