import math

def approx_cosh(x, n):
    result = 0
    for k in range(n + 1):
        term = (x**(2 * k)) / math.factorial(2 * k)
        result += term
    return result

# Test cases
assert round(approx_cosh(x=1, n=10), 2) == 1.54
print(round(approx_cosh(x=3.14, n=10), 2))
