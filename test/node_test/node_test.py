__author__ = 'yuczhou'

import unittest

from timer.node.node import Node
from timer.coordinate.coordinate import Coordinate as Coord


class NodeTest(unittest.TestCase):
    def test_init(self):
        node = Node(Coord([1, 1]))
        self.assertEqual(node.coord, Coord([1, 1]))

    def test_add_neighbor(self):
        node = Node(Coord([1, 1]))
        node[1] = Node(Coord([1, 2]))
        self.assertEqual(len(node), 1)

    def test_eq(self):
        node = Node(Coord([1, 1]))
        node[1] = Node(Coord([1, 2]))
        node[2] = Node(Coord([1, 3]))
        node[3] = Node(Coord([1, 4]))
        self.assertTrue(node == node)

    def test_iterator(self):
        node = Node(Coord([1, 1]))
        node[1] = Node(Coord([1, 2]))
        node[2] = Node(Coord([1, 3]))
        node[3] = Node(Coord([1, 4]))
        for neighbor in node:
            self.assertIn(neighbor, node)


if __name__ == '__main__':
    unittest.main()
