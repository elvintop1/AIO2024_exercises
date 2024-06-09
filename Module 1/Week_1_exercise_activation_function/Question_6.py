import math

def calc_activation_func(x, act_name):
    if act_name == 'sigmoid':
        return 1 / (1 + math.exp(-x))
    elif act_name == 'relu':
        return max(0, x)
    elif act_name == 'elu':
        return x if x >= 0 else math.exp(x) - 1
    else:
        raise ValueError("Unsupported activation function")

# Test cases
assert calc_activation_func(x=1, act_name='relu') == 1
print(round(calc_activation_func(x=3, act_name='sigmoid'), 2))
