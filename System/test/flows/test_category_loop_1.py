from workflow.pipelines.category_loop import CategoryLoopEngine


def test_category_loop_engine():
    engine = CategoryLoopEngine(min_confidence=85, max_attempts=3)

    # Evento chiaramente NON stagionale (verrà classificato N/A)
    title = "Autumn Festival | Dance Show"
    themes = ["dance", "contemporary", "festival"]
    summary = "A modern dance performance featuring local artists."

    result = engine.run(title, themes, summary)

    print("\n=== CATEGORY LOOP ENGINE RESULT ===")
    print("Final category:", result.get("category"))
    print("Score:", result.get("score"))
    print("Attempts:", result.get("attempts"))
    print("Excluded category:", result.get("excluded_category"))
    print("Success:", result.get("success"))
    print("Fallback:", result.get("fallback", False))

    print("\nFull Result:", result)


if __name__ == "__main__":
    test_category_loop_engine()
