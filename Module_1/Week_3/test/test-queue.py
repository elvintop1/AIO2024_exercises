import unittest
from Module_1.Week_3.Queue_implement import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue(capacity=3)

    def test_initialization(self):
        self.assertEqual(self.queue.capacity, 3)
        self.assertTrue(self.queue.is_empty())
        self.assertFalse(self.queue.is_full())

    def test_enqueue(self):
        self.queue.list.clear()
        self.queue.enqueue(1)
        self.assertEqual(self.queue.front(), 1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.front(), 1)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.front(), 1)
        self.assertTrue(self.queue.is_full())

    def test_enqueue_overflow(self):
        self.queue.list.clear()
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        with self.assertRaises(AssertionError) as context:
            self.queue.enqueue(4)
            self.assertEqual(str(context.exception), "The list is full")

    def test_dequeue(self):
        self.queue.list.clear()
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.dequeue()
        self.assertEqual(self.queue.front(), 2)
        self.queue.dequeue()
        self.assertEqual(self.queue.front(), 3)
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())

    def test_dequeue_underflow(self):
        self.queue.list.clear()
        with self.assertRaises(AssertionError) as context:
            self.queue.dequeue()
            self.assertEqual(str(context.exception), "The list is empty")

    def test_front(self):
        self.queue.list.clear()
        self.queue.enqueue(1)
        self.assertEqual(self.queue.front(), 1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.front(), 1)
        self.queue.dequeue()
        self.assertEqual(self.queue.front(), 2)

    def test_is_empty(self):
        self.queue.list.clear()
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())

    def test_is_full(self):
        self.queue.list.clear()
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertFalse(self.queue.is_full())
        self.queue.enqueue(3)
        self.assertTrue(self.queue.is_full())

if __name__ == "__main__":
    unittest.main()