import json
from workflow.database.db import get_connection


class EventSaver:

    def save(self, context: dict) -> None:
        conn = get_connection()
        cur = conn.cursor()

        data = (
            context.get("id"),
            context.get("slug"),
            context.get("title"),
            context.get("description"),
            context.get("summary"),
            json.dumps(context.get("themes")),
            context.get("category_final"),
            context.get("category_score"),
            context.get("category_attempts"),
            context.get("category_excluded"),
            1 if context.get("category_loop_success") else 0,
            json.dumps(context.get("errors")),
            json.dumps(context.get("event_raw")),
        )

        cur.execute("""
            INSERT INTO events_processed (
                event_id, slug, title, description, summary, themes,
                category_final, category_score, category_attempts,
                category_excluded, loop_success, errors, raw_event
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(event_id, slug) DO UPDATE SET
                title=excluded.title,
                description=excluded.description,
                summary=excluded.summary,
                themes=excluded.themes,
                category_final=excluded.category_final,
                category_score=excluded.category_score,
                category_attempts=excluded.category_attempts,
                category_excluded=excluded.category_excluded,
                loop_success=excluded.loop_success,
                errors=excluded.errors,
                raw_event=excluded.raw_event;
        """, data)

        conn.commit()
        conn.close()
