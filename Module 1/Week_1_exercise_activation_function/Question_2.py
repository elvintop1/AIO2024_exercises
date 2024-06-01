import math

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

# Test cases
assert is_number(3) == True
assert is_number('-2a') == False
print(is_number(1))
print(is_number('n'))
