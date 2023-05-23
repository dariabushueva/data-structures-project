"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue, Node

class TestStack(unittest.TestCase):

    def test_node(self):
        n1 = Node(10, None)
        n2 = Node(20, n1)
        self.assertEqual(n1.data, 10)
        self.assertEqual(n2.data, 20)
        self.assertEqual(n1.next_node, None)

    def test_queue(self):
        queue = Queue()
        self.assertEqual(queue.head, None)
        self.assertEqual(queue.tail, None)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert str(queue) == "1\n2\n3"
        self.assertEqual(queue.head.data, 1)
        self.assertEqual(queue.tail.data, 3)
        queue.dequeue()
        self.assertEqual(queue.head.data, 2)
        self.assertEqual(queue.tail.data, 3)
        queue.dequeue()
        self.assertEqual(queue.head.data, 3)
        self.assertEqual(queue.tail.data, 3)
        queue.dequeue()
        self.assertEqual(queue.head, None)
        self.assertEqual(queue.tail, None)
        assert str(queue) == ""
