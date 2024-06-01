import math

def approx_sinh(x, n):
    result = 0
    for k in range(n + 1):
        term = (x**(2 * k + 1)) / math.factorial(2 * k + 1)
        result += term
    return result

# Test cases
assert round(approx_sinh(x=1, n=10), 2) == 1.18
print(round(approx_sinh(x=3.14, n=10), 2))
