### INPUT
title: {title}
main_themes: {themes}
short_description: {summary}
assigned_category: {assigned_category}

### ALLOWED CATEGORIES

You must evaluate the assigned category strictly against the following allowed categories:

- Winter
- Autumn
- Spring
- Summer
- N/A   (Non-seasonal event)

If the assigned_category is NOT one of these allowed categories, you must assign a confidence score of **0** automatically.

This rule overrides any other principle.

### PRIMARY TASK

Your task is to provide a confidence score (from 0 to 100) that quantifies how accurately the assigned_category reflects the event's true nature, based on the principles below. 

## EVALUATION PRINCIPLES

1. ABSOLUTE EXCLUSION RULE: DATE IS IRRELEVANT 
You MUST categorically ignore any date, month, or time reference (e.g., "October 22," "mid-July," "December weekend"). The evaluation is based EXCLUSIVELY on the event's thematic content (what it is about), not when it occurs.

-Correct Example: An event about a "chestnut festival" IS thematically "Autumn".

-Incorrect Example: An "Simphonic Orchestra" event held on "October 22" is NOT thematically "Autumn" despite is held in October.

2.THE SKEPTICISM PRINCIPLE: A Seasonal Name Does NOT Equal a Seasonal Theme This is your most important rule. If a seasonal word (e.g., "Autumn", "Summer") appears in the title or main_themes, your default assumption is that it is non-thematic. You must then verify this assumption by analyzing the short_description.

VALIDATION TEST: Ask yourself: "Is the core activity described (e.g., a dance performance, a tech conference, an art exhibition) intrinsically and exclusively seasonal?"

If the answer is NO, then the seasonal word is just a label. You MUST ignore it and treat the event's true theme as N/A.

If the answer is YES (e.g., the activity is a chestnut festival or christmas market), then the seasonal theme is confirmed.

3. CONTEXT IS SOVEREUGN

The dominant themes and overall purpose of the event always have priority over isolated keywords mentioned in a secondary context.

3. PROOF MUST BE TEMATIC AND UNAMBIGUOUS 

High confidence requires undeniable proof within the event's themes. The **absence of seasonal thematic proof** is very **strong evidence in favor of the "N/A" category**.

**SCORING LOGIC**

Score 90-100 (Perfect Match):

-Case A (Correctly Seasonal): The assigned_category is a season (e.g., Autumn) AND the main_themes contain intrinsically seasonal keywords (e.g., christmas, grape harvest, carnival, chestnuts, mushroom festival).

-Case B (Correctly Non-Seasonal): The assigned_category is N/A AND the main_themes are generic (e.g., food, art, music, culture, tech) with a clear absence of any seasonal themes and A seasonal keyword exists but was correctly identified as non-thematic by the Skepticism Principle (e.g., an "Autumn Festival" which is a contemporary dance event).

Score 1-79 (Weak or Flawed Match):

-Case A (Superficial Link): The assigned_category is a season but is based on a non-thematic word (e.g., assigned_category: "Autumn" for a "classical music" event simply titled "Autumn Festival"). The seasonality is in name only, not in theme.

-Case B (Missed Seasonal Link): The assigned_category is N/A, but the main_themes contain clear, intrinsic seasonal keywords that were ignored.

Score 0 (Direct Contradiction):

The assigned_category is in blatant, direct opposition to the event's themes (e.g., assigned_category: "Summer" for an event with the theme christmas markets).

######################################################################################################################################

APPLIED EXAMPLES
Example 1: The Critical False Positive (Correctly identified as N/A)

Input:

title: "Autumn Festival | Smile"

main_themes: autumn festival, dance, contemporary dance

short_description: "A new contemporary dance production by Ocram Dance Movement..."

assigned_category: N/A

AI's Reasoning: The title contains "Autumn". I must apply the Skepticism Principle. The core activity is "contemporary dance", which is not intrinsically autumnal. Therefore, the word "Autumn" is a non-thematic label and must be ignored. The event's true nature is non-seasonal. The assigned_category N/A is correct.

Expected Score: 98

Example 2: The Truly Seasonal Event (Correctly identified)

Input:

title: "Christmas Markets in the Square"

main_themes: christmas, markets, crafts, typical sweets

short_description: "Market stalls with local crafts, traditional sweets, and Christmas decorations."

assigned_category: Winter

AI's Reasoning: The theme christmas is intrinsically seasonal. The Skepticism Principle is not violated because the core activity is directly tied to the season. The assigned_category Winter is a perfect match.

Expected Score: 100

Example 3: The Flawed Match (Incorrectly assigned)

Input:

title: "Autumn Festival | Smile"

main_themes: autumn festival, dance, contemporary dance

short_description: "A new contemporary dance production..."

assigned_category: Autumn

AI's Reasoning: The assigned_category is Autumn. However, the Skepticism Principle shows that the core activity (dance) is not seasonal. The assignment is based on a superficial, non-thematic keyword. This is a flawed match.

Expected Score: 25
