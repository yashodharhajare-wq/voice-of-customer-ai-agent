from collections import Counter
import pandas as pd

df = pd.read_pickle(
    r"C:\Users\yasho\Desktop\Mechanical Keyboard AI agent\outputs\normalized_insights.pkl"
)


def add_to_counter(counter, items):
    """
    Handles:
    - ["Wireless", "QMK"]
    - [{"layout": "15 Units Width"}]
    - mixed lists
    """

    if not items:
        return

    for item in items:

        # Normal string item
        if isinstance(item, str):
            counter[item] += 1

        # Dictionary item
        elif isinstance(item, dict):
            for value in item.values():

                if isinstance(value, str):
                    counter[value] += 1

                elif isinstance(value, list):
                    for v in value:
                        if isinstance(v, str):
                            counter[v] += 1

        # List item
        elif isinstance(item, list):
            for v in item:
                if isinstance(v, str):
                    counter[v] += 1

        # Fallback
        else:
            counter[str(item)] += 1


pain_point_counter = Counter()
gain_counter = Counter()
personas_counter = Counter()
must_have_features_counter = Counter()
nice_to_have_features_counter = Counter()
feature_requests_counter = Counter()

for _, row in df.iterrows():

    add_to_counter(
        pain_point_counter,
        row.get("pain_points", [])
    )

    add_to_counter(
        gain_counter,
        row.get("gains", [])
    )

    add_to_counter(
        personas_counter,
        row.get("personas", [])
    )

    add_to_counter(
        must_have_features_counter,
        row.get("must_have_features", [])
    )

    add_to_counter(
        nice_to_have_features_counter,
        row.get("nice_to_have_features", [])
    )

    add_to_counter(
        feature_requests_counter,
        row.get("feature_requests", [])
    )

print("Total discussions:", len(df))

print(
    "Discussions with pain points:",
    (df["pain_points"].apply(lambda x: len(x) if isinstance(x, list) else 0) > 0).sum()
)

print(
    "Discussions with gains:",
    (df["gains"].apply(lambda x: len(x) if isinstance(x, list) else 0) > 0).sum()
)

print(
    "Discussions with feature requests:",
    (df["feature_requests"].apply(lambda x: len(x) if isinstance(x, list) else 0) > 0).sum()
)

print("\nTOP PAIN POINTS\n")

for item, count in pain_point_counter.most_common(20):
    print(count, "-", item)

print("\nTOP GAINS\n")

for item, count in gain_counter.most_common(20):
    print(count, "-", item)

print("\nTOP FEATURE REQUESTS\n")

for item, count in feature_requests_counter.most_common(20):
    print(count, "-", item)

print("\nTOP PERSONAS\n")

for item, count in personas_counter.most_common(20):
    print(count, "-", item)

print("\nTOP MUST-HAVE FEATURES\n")

for item, count in must_have_features_counter.most_common(20):
    print(count, "-", item)

print("\nTOP NICE-TO-HAVE FEATURES\n")

for item, count in nice_to_have_features_counter.most_common(20):
    print(count, "-", item)