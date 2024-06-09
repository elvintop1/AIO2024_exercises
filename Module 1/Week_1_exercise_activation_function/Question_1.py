import math

def calc_f1_score(tp, fp, fn):
    if tp + fp == 0 or tp + fn == 0:
        return 0.0  # Handle edge case where there is no positive prediction or no true positive
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    if precision + recall == 0:
        return 0.0  # Handle edge case where precision and recall are both zero
    f1_score = 2 * (precision * recall) / (precision + recall)
    return f1_score

# Test cases
assert round(calc_f1_score(tp=2, fp=3, fn=5), 2) == 0.33
print(round(calc_f1_score(tp=2, fp=4, fn=5), 2))
