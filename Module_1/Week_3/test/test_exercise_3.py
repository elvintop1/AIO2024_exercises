import unittest
from Module_1.Week_3.Stack_implement import Stack

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack(capacity=3)

    def test_initialization(self):
        self.assertEqual(self.stack.capacity, 3)
        self.assertTrue(self.stack.is_empty())
        self.assertFalse(self.stack.is_full())

    def test_push(self):
        self.stack.list.clear()
        self.stack.push(1)
        self.assertEqual(self.stack.top(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.top(), 2)
        self.stack.push(3)
        self.assertEqual(self.stack.top(), 3)
        self.assertTrue(self.stack.is_full())

    def test_push_overflow(self):
        self.stack.list.clear()
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        with self.assertRaises(AssertionError) as context:
            self.stack.push(4)
            self.assertEqual(str(context.exception), "The list is full")

    def test_pop(self):
        self.stack.list.clear()
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.pops()
        self.assertEqual(self.stack.top(), 2)
        self.stack.pops()
        self.assertEqual(self.stack.top(), 1)
        self.stack.pops()
        self.assertTrue(self.stack.is_empty())

    def test_pop_underflow(self):
        self.stack.list.clear()
        with self.assertRaises(AssertionError) as context:
            self.stack.pops()
            self.assertEqual(str(context.exception), "The list is empty")

    def test_top(self):
        self.stack.list.clear()
        self.stack.push(1)
        self.assertEqual(self.stack.top(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.top(), 2)
        self.stack.pops()
        self.assertEqual(self.stack.top(), 1)

    def test_is_empty(self):
        self.stack.list.clear()
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_is_full(self):
        self.stack.list.clear()
        self.stack.push(1)
        self.stack.push(2)
        self.assertFalse(self.stack.is_full())
        self.stack.push(3)
        self.assertTrue(self.stack.is_full())

if __name__ == "__main__":
    unittest.main()