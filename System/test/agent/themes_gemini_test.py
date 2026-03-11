from workflow.agents.themes_agent import ThemesAgent

agent = ThemesAgent()

def test_themes_christmas_market():
    title = "Christmas Market in the Old Town"
    desc = (
        "The historic old town is transformed into a bright and colorful "
        "Christmas village featuring artisan stalls, handcrafted wooden toys, "
        "local pastries, mulled wine, live music, and interactive installations. "
        "Visitors can walk through narrow medieval streets illuminated by warm "
        "decorative lights and enjoy performances by local choirs."
    )
    
    tags = agent.run(title, desc)
    print("\n[Test 1] Christmas Market Tags:", tags)


def test_themes_summer_music_festival():
    title = "Summer Music Festival by the Seaside"
    desc = (
        "A three-day open-air festival set on the seaside promenade featuring "
        "international rock bands, emerging indie artists, electronic DJs, "
        "food trucks offering local seafood, and immersive light shows at night. "
        "Workshops, jam sessions, and dance areas allow attendees to engage "
        "directly with performers."
    )
    
    tags = agent.run(title, desc)
    print("\n[Test 2] Summer Music Festival Tags:", tags)


def test_themes_food_fair():
    title = "Traditional Food and Culture Fair"
    desc = (
        "A celebration of regional culinary heritage including tasting stands, "
        "cooking demonstrations, masterclasses with renowned chefs, exhibitions "
        "on ancient farming techniques, and reenactments of rural traditions. "
        "Visitors can try handmade pasta, artisan cheeses, cured meats, wines, "
        "and listen to folk groups performing traditional dances."
    )

    tags = agent.run(title, desc)
    print("\n[Test 3] Food Fair Tags:", tags)


def run_all():
    test_themes_christmas_market()
    test_themes_summer_music_festival()
    test_themes_food_fair()


if __name__ == "__main__":
    run_all()
