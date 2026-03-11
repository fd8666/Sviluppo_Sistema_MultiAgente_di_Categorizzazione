from workflow.agents.summary_agent import SummaryAgent

agent = SummaryAgent()

def test_summary_festival_of_lights():
    title = "Festival of Lights"
    content = (
        "The entire old town becomes a luminous stage during the Festival of Lights. "
        "Massive projections animate the facades of historical buildings with shifting "
        "colors, abstract shapes, and scenes inspired by local folklore. Interactive "
        "light tunnels, motion-activated installations, and illuminated sculptures lead "
        "visitors on a sensory journey through alleyways and squares. Performers dressed "
        "in LED-enhanced costumes dance among the crowd, while atmospheric music creates "
        "an immersive environment. The event blends tradition and innovation, offering a "
        "deeply emotional nighttime experience."
    )
    
    summary = agent.run(title, content)
    print("\n[Summary 1] Festival of Lights:\n", summary)


def test_summary_modern_art_exhibition():
    title = "Contemporary Art Exhibition – Identity in Motion"
    content = (
        "The exhibition explores themes of identity, transformation, and perception "
        "through multimedia installations, video art, and conceptual sculptures. "
        "Artists from various cultural backgrounds present works reflecting the fluidity "
        "of modern self-expression. Visitors move through immersive rooms where mirrors, "
        "digital projections, and soundscapes blur the boundaries between the observer "
        "and the observed. Interactive pieces encourage participation, challenging "
        "conventional notions of authorship and audience."
    )

    summary = agent.run(title, content)
    print("\n[Summary 2] Contemporary Art Exhibition:\n", summary)


def test_summary_ai_conference():
    title = "International Conference on Artificial Intelligence"
    content = (
        "Leading experts, researchers, and innovators gather for a three-day program of "
        "keynote speeches, panel discussions, and technical workshops. Topics include "
        "ethical AI, robotics, machine learning applications in medicine and climate "
        "science, and the future of human-AI collaboration. Demonstration areas allow "
        "attendees to interact with prototypes, experimental models, and cutting-edge "
        "technologies developed by universities and startups."
    )

    summary = agent.run(title, content)
    print("\n[Summary 3] AI Conference:\n", summary)


def run_all():
    test_summary_festival_of_lights()
    test_summary_modern_art_exhibition()
    test_summary_ai_conference()


if __name__ == "__main__":
    run_all()
