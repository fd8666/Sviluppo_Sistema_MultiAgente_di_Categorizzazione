from workflow.agents.evaluator_agent import EvaluatorAgent

agent = EvaluatorAgent()


def test_eval_high_confidence_winter():
    # Caso perfetto: Natale -> Inverno.
    # Ci aspettiamo un punteggio > 90.
    
    title = "Christmas Market by the Cathedral"
    themes = [
        "christmas", "lights", "decorations",
        "mulled wine", "artisan crafts"
    ]
    summary = (
        "A seasonal event focused entirely on Christmas traditions, with "
        "decorations, festive lights, and winter-themed products."
    )
    assigned_category = "Winter"

    score = agent.run(title, themes, summary, assigned_category)
    print("\n[Eval 1] High Confidence Winter:", score)


def test_eval_high_confidence_na():
    
    # Caso neutro: nessuna connessione stagionale.
    
    title = "Tech Innovation Forum"
    themes = [
        "innovation", "robotics", "startups",
        "science", "technology"
    ]
    summary = (
        "A large forum bringing together innovators and researchers to discuss "
        "AI, robotics, and technological advancements."
    )
    assigned_category = "N/A"

    score = agent.run(title, themes, summary, assigned_category)
    print("\n[Eval 2] High Confidence N/A:", score)


def test_eval_low_confidence_mismatch():
    
    # Caso sbagliato: festival autunnale assegnato come estate.
    
    title = "Chestnut Harvest Festival"
    themes = [
        "chestnuts", "harvest", "forest", 
        "local food", "autumn"
    ]
    summary = (
        "An event centered on the chestnut harvest and traditional autumn "
        "food practices."
    )
    assigned_category = "Summer"

    score = agent.run(title, themes, summary, assigned_category)
    print("\n[Eval 3] Low Confidence Mismatch:", score)


def test_eval_ambiguous():
    
    # Caso ambiguo: titolo suggerisce una stagione, contenuti neutri.
    
    title = "Spring Art Walk"
    themes = [
        "art exhibition", "galleries", "installation", 
        "urban culture", "artists"
    ]
    summary = (
        "A curated walk across contemporary art galleries in the city. "
        "Despite the word 'spring' in the title, no seasonal themes are present."
    )
    assigned_category = "Spring"

    score = agent.run(title, themes, summary, assigned_category)
    print("\n[Eval 4] Ambiguous Assignment:", score)


def run_all():
    test_eval_high_confidence_winter()
    test_eval_high_confidence_na()
    test_eval_low_confidence_mismatch()
    test_eval_ambiguous()


if __name__ == "__main__":
    run_all()
