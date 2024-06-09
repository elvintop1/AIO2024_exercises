import math

def calc_elu(x, alpha=0.01):
    if x <= 0:
        return alpha * (math.exp(x) - 1)
    else:
        return x

# Test cases
assert round(calc_elu(1)) == 1
print(round(calc_elu(-1), 2))
