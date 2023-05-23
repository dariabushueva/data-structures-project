import unittest
from src.stack import Stack, Node


class TestStack(unittest.TestCase):

    def test_node(self):
        n1 = Node(10, None)
        n2 = Node(20, n1)
        self.assertEqual(n1.data, 10)
        self.assertEqual(n2.data, 20)
        self.assertEqual(n1.next_node, None)

    def test_stack(self):
        stack = Stack()
        assert str(stack) == ""
        self.assertEqual(stack.top, None)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert str(stack) == "3\n2\n1"
        self.assertEqual(stack.top.data, 3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.top.next_node.data, 1)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.top.next_node, None)







