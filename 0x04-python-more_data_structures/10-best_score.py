#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_key = next(iter(a_dictionary))
    max_value = a_dictionary[max_key]

    for key, value in a_dictionary.items():
        if value > max_value:
            max_key, max_value = key, value

    return max_key
