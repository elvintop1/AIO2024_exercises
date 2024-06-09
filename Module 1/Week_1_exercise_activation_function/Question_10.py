import math

def approx_sin(x, n):
    result = 0
    for k in range(n + 1):
        term = ((-1)**k) * (x**(2 * k + 1)) / math.factorial(2 * k + 1)
        result += term
    return result

# Test cases
assert round(approx_sin(x=1, n=10), 4) == 0.8415
print(round(approx_sin(x=3.14, n=10), 4))
