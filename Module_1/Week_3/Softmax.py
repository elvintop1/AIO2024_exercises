import torch
import torch.nn as nn

class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        return exp_x / torch.sum(exp_x)

class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        max_x = torch.max(x)
        exp_x = torch.exp(x - max_x)
        return exp_x / torch.sum(exp_x)

# Examples
data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)  # tensor([0.0900, 0.2447, 0.6652])

data = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
print(output)  # tensor([0.0900, 0.2447, 0.6652])
