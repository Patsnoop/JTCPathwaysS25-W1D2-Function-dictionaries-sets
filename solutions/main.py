def count_occurrences(items: list) -> dict:
    result = {}
    for item in items:
        result[item] = result.get(item, 0) + 1
    return result

def unique_items(set1: set, set2: set) -> set:
    return set1.symmetric_difference(set2)