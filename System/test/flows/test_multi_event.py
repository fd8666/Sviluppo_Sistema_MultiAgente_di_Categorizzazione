from workflow.pipelines.multi_event_flow import build_multi_event_flow


def test_multi_event_pipeline():
    pipeline = build_multi_event_flow()

    print("\n=== START MULTI-EVENT PIPELINE TEST ===\n")

    results = pipeline.run(page=1)

    print("\n=== MULTI-EVENT RESULTS SUMMARY ===")
    print("Total events processed:", len(results))

    for idx, result in enumerate(results, start=1):
        print(f"\n================= EVENT {idx} =================")

        print("ID:", result.get("id"))
        print("Title:", result.get("title"))
        print("Slug:", result.get("slug"))

        print("\nSummary:", result.get("summary"))
        print("Themes:", result.get("themes"))

        print("\nFinal Category:", result.get("category_final"))
        print("Score:", result.get("category_score"))
        print("Attempts:", result.get("category_attempts"))
        print("Excluded category:", result.get("category_excluded_previous"))
        print("Loop Success:", result.get("category_loop_success"))

        print("\nErrors:", result.get("errors"))

    print("\n=== END MULTI-EVENT PIPELINE TEST ===")


if __name__ == "__main__":
    test_multi_event_pipeline()
