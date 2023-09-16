#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if len(a_dictionary) == 0:
        return None
    score = []
    for key, value in a_dictionary.items():
        score.append(value)
    score.sort()
    bn = len(score) - 1
    for k, v in a_dictionary.items():
        if v == score[bn]:
            key = k
    return key
