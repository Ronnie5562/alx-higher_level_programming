#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""

    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    a = [a_dictionary[x] for x in a_dictionary]
    return max(a)