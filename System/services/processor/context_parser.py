import re

REGEX_PULIZIA_HTML = re.compile(r"<[^>]+>")

class ContextParser:
    """
    Parser universale che funziona sia per API che CSV.
    Estrae: id, title, slug, description
    """

    @staticmethod
    def remove_html(html: str) -> str:
        if not html:
            return ""
        text = REGEX_PULIZIA_HTML.sub(" ", html)
        return " ".join(text.split()).strip()

    def parse(self, event: dict) -> dict:

        # --- ID ---
        event_id = (
            event.get("id")
            or event.get("IdEvento")  # caso CSV alternativo
            or event.get("event_id")
        )

        # --- TITLE ---
        # Struttura API: body.title
        # Struttura CSV: title
        title = (
            event.get("title")
            or event.get("Titolo")
            or (event.get("body", {}) or {}).get("title")
            or ""
        ).strip()

        # --- SLUG ---
        slug = (
            event.get("slug")
            or (event.get("body", {}) or {}).get("slug")
            or None
        )

        # --- DESCRIPTION ---
        raw_description = (
            event.get("description")                 # CSV
            or event.get("Descrizione")              # CSV variant
            or (event.get("body", {}) or {}).get("content")  # API
            or ""
        )

        # Descrizione può essere dict con "html"
        if isinstance(raw_description, dict):
            raw_description = raw_description.get("html", "")

        description_clean = self.remove_html(raw_description)

        return {
            "id": event_id,
            "title": title,
            "slug": slug,
            "description": description_clean,
        }
