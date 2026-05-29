from collections import Counter


def count_items(df, column):

    counter = Counter()

    for values in df[column]:

        if not values:
            continue

        for item in values:

            if isinstance(item, str):
                counter[item] += 1

            elif isinstance(item, dict):

                for value in item.values():

                    if isinstance(value, str):
                        counter[value] += 1

                    elif isinstance(value, list):

                        for v in value:

                            if isinstance(v, str):
                                counter[v] += 1

            elif isinstance(item, list):

                for v in item:

                    if isinstance(v, str):
                        counter[v] += 1

            else:
                counter[str(item)] += 1

    return counter