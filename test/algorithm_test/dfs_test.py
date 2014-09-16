from timer.algorithm.dfs import DFS
from timer.coordinate.coordinate import Coordinate
from timer.node.gate import Gate
from timer.node.node import Node
from timer.vlsi.electro_property import ElectroProperty

__author__ = 'yuczhou'

import unittest


class DFSTest(unittest.TestCase):

    def setUp(self):
        self._root_gate = Gate(Coordinate([1, 0]), ElectroProperty([4, 0]))
        self._root_gate[1] = Node(Coordinate([1, 5]))
        self._root_gate[1][3] = Gate(Coordinate([1, 13]), ElectroProperty([0, 8]))
        self._root_gate[2] = Gate(Coordinate([1, 6]), ElectroProperty([0, 7]))

        self._root_node = Node(Coordinate([1, 0]))
        self._root_node[1] = Node(Coordinate([1, 5]))
        self._root_node[2] = Node(Coordinate([1, 6]))

        self._unit_rc = ElectroProperty([1, 1])

    def test_root_gate(self):
        self.assertEqual(DFS(self._root_gate, self._unit_rc).delay()[0], 176.5 + 96)


if __name__ == '__main__':
    unittest.main()
