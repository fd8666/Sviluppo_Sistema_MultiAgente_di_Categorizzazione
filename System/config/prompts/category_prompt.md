### INPUT
title: {title}
main_themes: {themes}
short_description: {summary}
excluded_categories: {excluded_category}

### ADDITIONAL CONSTRAINT

- If `excluded_category` is not "None", you MUST NOT return that category in your final answer for this iteration, even if it might seem acceptable.
- If `excluded_category` is "None", ignore this constraint.

## CORE PRINCIPLE: The Rule of Thematic Relevance

An event is considered seasonal only if its core activities, products, or themes are intrinsically and exclusively linked to a specific season. A mere mention of a season in the title (e.g., "Summer Concert") is NOT sufficient evidence if the activity itself (e.g., a classical music concert) could take place in any other season.

## INSTRUCTIONS:
-1 Analyze main_themes First: This is your primary source of truth. Scrutinize the list for concrete, unambiguous seasonal keywords (e.g., chestnuts, harvest, christmas, easter, beach, carnival, snow). These have the highest priority.

-2 Perform the Skepticism Test: Read the title and short_description.

If the title contains a seasonal reference (e.g., "Autumn Festival"), you must critically ask: "Do the main_themes or short_description provide undeniable proof that the event's CORE ACTIVITY is exclusively seasonal?"

 .If YES (e.g., the description is about grape harvesting), the thematic link is confirmed.

 .If NO (e.g., the description is about a generic art exhibition), the event is NOT seasonal. You must ignore the seasonal reference in the title as misleading.

-3 Final Decision Logic:

IF Step 1 or 2 provides clear, explicit, and undeniable thematic evidence of seasonality, select the most appropriate category.

ELSE, in ALL other cases, or if you have even the slightest doubt, your mandatory and final answer MUST BE "N/A".

######################################################################################################################################

## APPLIED EXAMPLES (Demonstrating the reasoning process)

Example 1: False Positive

Input:

title: "Autumn Festival | Mozart Symphony Orchestra"
main_themes: classical music, orchestra, theatre, culture
short_description: "Performance by the Mozart Symphony Orchestra at the Rendano Theatre."

AI's Reasoning: The title mentions "Autumn". However, the main_themes and description are about classical music. A symphony concert is not an intrinsically autumnal activity; it can happen any time. The Rule of Thematic Relevance is not met. I must ignore the title's reference.

Expected Output: N/A

Example 2: True Positive (Confirmed by Theme)

Input:

title: "Autumn Sagra: The First Harvest"
main_themes: food, wine, harvest, local products, autumn
short_description: "Let's celebrate the season's first grape harvest together with tastings of new wine and local products."

AI's Reasoning: The title mentions "Autumn". The theme harvest and the description's focus on "grape harvest" are intrinsically and exclusively linked to the autumn season. The rule is met.

Expected Output: Autumn

Example 3: True Positive (Obvious Case)

Input:

title: "Christmas Markets in the Square"
main_themes: Christmas, markets, crafts, typical sweets
short_description: "Market stalls with local crafts, traditional sweets, and Christmas decorations."

AI's Reasoning: The theme Christmas is unambiguously seasonal. Thematic relevance is self-evident.

Expected Output: Winter