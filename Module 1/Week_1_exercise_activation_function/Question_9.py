import math

def approx_cos(x, n):
    result = 0
    for k in range(n + 1):
        term = ((-1)**k) * (x**(2 * k)) / math.factorial(2 * k)
        result += term
    return result

# Test cases
assert round(approx_cos(x=1, n=10), 2) == 0.54
print(round(approx_cos(x=3.14, n=10), 2))
