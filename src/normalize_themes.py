import json
import pandas as pd
import requests

print("Loading discussion insights...")

df = pd.read_pickle(
    r"C:\Users\yasho\Desktop\Mechanical Keyboard AI agent\outputs\discussion_insights.pkl"
)

MODEL = "qwen2.5:7b"

results = []

PERSONA_MAP = {
    "gamer": "Gamers",
    "gamers": "Gamers",

    "keyboard enthusiast": "Keyboard Enthusiasts",
    "keyboard enthusiasts": "Keyboard Enthusiasts",
    "mechanical keyboard enthusiast": "Keyboard Enthusiasts",
    "mechanical keyboard enthusiasts": "Keyboard Enthusiasts",
    "keyboard user": "Keyboard Enthusiasts",
    "keyboard users": "Keyboard Enthusiasts",

    "custom builder": "Custom Builders",
    "custom builders": "Custom Builders",
    "keyboard builder": "Custom Builders",
    "custom keyboard builder": "Custom Builders",

    "programmer": "Programmers",
    "programmers": "Programmers",

    "office worker": "Office Workers",
    "office workers": "Office Workers",

    "network engineer": "Network Engineers",
    "network engineers": "Network Engineers",
}


def normalize_personas(personas):

    normalized = []

    for p in personas:

        key = str(p).strip().lower()

        normalized.append(
            PERSONA_MAP.get(
                key,
                p
            )
        )

    return list(dict.fromkeys(normalized))

def clean_themes(items):

    BAD_THEMES = {
        "feature request",
        "feature requests",
        "pain point",
        "pain points",
        "gain",
        "gains",
        "problem",
        "problems",
        "issue",
        "issues",
        "benefit",
        "benefits",
        "persona",
        "personas",
    }

    cleaned = []

    for item in items:

        value = str(item).strip()

        if value.lower() in BAD_THEMES:
            continue

        cleaned.append(value)

    return list(dict.fromkeys(cleaned))

for idx, row in df.iterrows():

    print(f"Processing {idx}")

    prompt = f"""
You are a Theme Normalizer.

CRITICAL NORMALIZATION RULES

A theme must represent a category, not a sentence.

Merge singular/plural variants:

Long Wait Time
Long Wait Times

→ Long Wait Time

Merge synonymous concepts:

Quiet Keyboard
Quiet Switches
Improved Sound Quality

→ Quiet Typing

Do not create generic themes:

Bad:
Feature Request
Pain Point
Gain
Issue
Problem

Good:
Wireless Support
QMK Compatibility
Switch Noise
Long Wait Time

A theme must be specific.

Do not place personas inside feature_requests.

Do not place feature requests inside personas.

Do not place gains inside pain_points.

Return only meaningful canonical themes.

Examples:

"Loud switches"
"Switches are too loud"
"Switch noise is annoying"

becomes

"Switch Noise"

---

"Typing IP addresses is difficult"
"Entering numbers on TKL is frustrating"

becomes

"Number Entry Difficulty"

Rules:

- Return concise themes
- Maximum 4 words per theme
- Merge duplicates aggressively
- Use consistent naming
- Return valid JSON only

PERSONA NORMALIZATION RULES

Use these persona labels whenever applicable:

- Keyboard Enthusiasts
- Gamers
- Programmers
- Office Workers
- Network Engineers
- Custom Builders

Examples:

Mechanical Keyboard Enthusiast -> Keyboard Enthusiasts
Mechanical Keyboard Enthusiasts -> Keyboard Enthusiasts
Keyboard User -> Keyboard Enthusiasts
Keyboard Users -> Keyboard Enthusiasts

Gamer -> Gamers

Keyboard Builder -> Custom Builders
Custom Keyboard Builder -> Custom Builders

Schema:

{{
  "pain_points": [],
  "gains": [],
  "personas": [],
  "must_have_features": [],
  "nice_to_have_features": [],
  "feature_requests": []
}}

INPUT:

{json.dumps({
    "pain_points": row["pain_points"],
    "gains": row["gains"],
    "personas": row["personas"],
    "must_have_features": row["must_have_features"],
    "nice_to_have_features": row["nice_to_have_features"],
    "feature_requests": row["feature_requests"]
}, indent=2)}
"""

    try:

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0
                }
            }
        )

        result = response.json()["response"]

        result = result.strip()

        if result.startswith("```json"):
            result = result.replace("```json", "", 1)

        if result.endswith("```"):
            result = result[:-3]

        result = result.strip()

        normalized = json.loads(result)

        normalized["pain_points"] = clean_themes(
            normalized.get("pain_points", [])
        )

        normalized["gains"] = clean_themes(
            normalized.get("gains", [])
        )

        normalized["must_have_features"] = clean_themes(
            normalized.get("must_have_features", [])
        )

        normalized["nice_to_have_features"] = clean_themes(
            normalized.get("nice_to_have_features", [])
        )

        normalized["feature_requests"] = clean_themes(
            normalized.get("feature_requests", [])
        )

        normalized["personas"] = normalize_personas(
            clean_themes(
                normalized.get("personas", [])
            )
        )

        results.append({
            "ID": row["ID"],
            "Title": row["Title"],

            # Discussion metadata
            "Post URL": row.get("Post URL"),
            "discussion_type": row.get("discussion_type"),
            "confidence": row.get("confidence"),
            "reason": row.get("reason"),

            # Engagement metadata
            "comment_count": row.get("comment_count"),
            "avg_score": row.get("avg_score"),
            "max_score": row.get("max_score"),

            "pain_points": clean_themes(normalized.get(
                "pain_points", []
            )),

            "gains": clean_themes(normalized.get(
                "gains", []
            )),

            "personas": normalized.get(
                "personas", []
            ),

            "must_have_features": clean_themes(normalized.get(
                "must_have_features", []
            )),

            "nice_to_have_features": clean_themes(normalized.get(
                "nice_to_have_features", []
            )),

            "feature_requests": clean_themes(normalized.get(
                "feature_requests", []
            ))
        })

    except Exception as e:

        print("ERROR:", e)

        results.append({
            "ID": row["ID"],
            "Title": row["Title"],

            "Post URL": row.get("Post URL"),
            "discussion_type": row.get("discussion_type"),
            "confidence": row.get("confidence"),
            "reason": row.get("reason"),

            "comment_count": row.get("comment_count"),
            "avg_score": row.get("avg_score"),
            "max_score": row.get("max_score"),

            # fallback to original values
            "pain_points": row["pain_points"],
            "gains": row["gains"],
            "personas": row["personas"],
            "must_have_features": row["must_have_features"],
            "nice_to_have_features": row["nice_to_have_features"],
            "feature_requests": row["feature_requests"],

            "error": str(e)
        })

normalized_df = pd.DataFrame(results)

normalized_df.to_pickle(
    r"C:\Users\yasho\Desktop\Mechanical Keyboard AI agent\outputs\normalized_insights.pkl"
)

print("\nSaved normalized_insights_V2.pkl")