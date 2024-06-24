import unittest
import torch
from torch import Tensor

from Module_1.Week_3.Softmax import SoftmaxStable, Softmax



class TestUnit(unittest.TestCase):

    def test_softmax(self) -> None:
        test_input: Tensor = torch.Tensor([1, 2, 3])
        func: Softmax = Softmax()
        output: Tensor = func(test_input)
        expected_output: Tensor = torch.tensor([0.0900, 0.2447, 0.6652])
        self.assertTrue(torch.allclose(output, expected_output, atol=1e-4))

    def test_softmax_stable(self) -> None:
        test_input: Tensor = torch.Tensor([1, 2, 3])
        func: SoftmaxStable = SoftmaxStable()
        output: Tensor = func(test_input)
        expected_output: Tensor = torch.tensor([0.0900, 0.2447, 0.6652])
        self.assertTrue(torch.allclose(output, expected_output, atol=1e-4))

if __name__ == "__main__":
    unittest.main()