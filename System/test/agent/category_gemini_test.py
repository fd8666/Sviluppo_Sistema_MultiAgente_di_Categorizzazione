from workflow.agents.category_agent import CategoryAgent

agent = CategoryAgent()


def test_category_autumn_harvest():
    # Caso molto chiaro: evento legato a un raccolto tipicamente autunnale.

    title = "Annual Chestnut Harvest Celebration"
    themes = [
        "chestnuts", "harvest", "forest traditions",
        "local food", "rural culture"
    ]
    summary = (
        "The celebration honors the chestnut harvest with traditional "
        "food stands, rural demonstrations, and forest-related activities "
        "typical of the autumn season."
    )

    result = agent.run(title, themes, summary)
    print("\n[Category 1] Autumn Harvest:", result)


def test_category_winter_christmas():
    # Caso chiaro: Natale -> Inverno.
   
    title = "Christmas Village and Artisan Fair"
    themes = [
        "christmas", "decorations", "crafts",
        "lights", "traditional sweets"
    ]
    summary = (
        "A festive village dedicated to Christmas traditions and winter-themed "
        "decorations, including artisan workshops and seasonal treats."
    )

    result = agent.run(title, themes, summary)
    print("\n[Category 2] Christmas/Winter:", result)


def test_category_non_seasonal_conference():
    # Caso non stagionale: conferenze, tecnologia, temi neutri.
    
    title = "International Robotics Conference"
    themes = [
        "robotics", "technology", "innovation",
        "science", "engineering"
    ]
    summary = (
        "A global conference focused on robotics research, AI systems, "
        "automation, and industrial innovation."
    )

    result = agent.run(title, themes, summary)
    print("\n[Category 3] Non-Seasonal (N/A):", result)


def test_category_false_seasonal_keyword():
    # Caso ambiguo: parola stagionale nel titolo ma NON nei contenuti.
    # Es: “Summer Jazz Nights” ma in realtà evento indoor, non stagionale.
    
    title = "Summer Jazz Nights"
    themes = [
        "jazz", "live music", "indoor concert",
        "performances", "artists"
    ]
    summary = (
        "A series of jazz concerts held indoors in theaters and cultural spaces. "
        "Despite the title, the themes are purely musical and not seasonal."
    )

    result = agent.run(title, themes, summary)
    print("\n[Category 4] False Seasonal Keyword (Expect N/A):", result)


def run_all():
    test_category_autumn_harvest()
    test_category_winter_christmas()
    test_category_non_seasonal_conference()
    test_category_false_seasonal_keyword()


if __name__ == "__main__":
    run_all()
