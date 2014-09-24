from timer.algorithm.dfs import DFS
from timer.coordinate.coordinate import Coordinate
from timer.node.buffer import Buffer
from timer.node.gate import Gate
from timer.node.node import Node
from timer.parser.line_parser.unit_rc_parser import UnitRCParser
from timer.vlsi.buffer_property import BufferProperty
from timer.vlsi.electro_property import ElectroProperty

__author__ = 'yuczhou'

import unittest


class DFSTest(unittest.TestCase):
    def setUp(self):
        self._root_gate = Gate(Coordinate([1, 0]), ElectroProperty([4, 0]))
        self._root_gate[1] = Node(Coordinate([1, 5]))
        self._root_gate[1][3] = Gate(Coordinate([1, 13]), ElectroProperty([0, 8]))
        self._root_gate[2] = Gate(Coordinate([1, 6]), ElectroProperty([0, 7]))

        self._unit_rc = ElectroProperty([1 / Coordinate.scale] * 2)

    def test_no_buffer(self):
        self.assertEqual(DFS(self._root_gate, self._unit_rc).delay()[0], 176.5 + 96)

    def test_simple_no_buffer(self):
        root = Gate(Coordinate([0, 0]), ElectroProperty([10, 0]))
        root[1] = Gate(Coordinate([10, 0]), ElectroProperty([0, 5]))

        unit_rc = ElectroProperty([1 / Coordinate.scale] * 2)

        self.assertEqual(DFS(root, unit_rc).delay()[0], 250)

    def test_simple_one_buffer(self):
        root = Gate(Coordinate([0, 0]), ElectroProperty([10, 0]))
        root[1] = Buffer(Coordinate([0, 0]), BufferProperty([10, 10], 0))
        root[1][1] = Gate(Coordinate([10, 0]), ElectroProperty([0, 5]))

        unit_rc = ElectroProperty([1 / Coordinate.scale] * 2)

        self.assertEqual(DFS(root, unit_rc).delay()[0], 350)

    def test_two_branch_one_buffer(self):
        root = Gate(Coordinate([0, 0]), ElectroProperty([10, 0]))
        root[1] = Node(Coordinate([5, 0]))
        root[1][1] = Gate(Coordinate([5, 0]), ElectroProperty([10, 10]))
        root[1][1][1] = Gate(Coordinate([10, 0]), ElectroProperty([0, 5]))
        root[1][2] = Gate(Coordinate([10, 5]), ElectroProperty([0, 10]))

        unit_rc = ElectroProperty([1 / Coordinate.scale] * 2)

        self.assertEqual(DFS(root, unit_rc).delay()[0], 662.5)

    def test_complex_case(self):
        root = Gate(Coordinate([0, 0]), ElectroProperty([5, 0]))
        root[1] = Node(Coordinate([0, 10]))
        root[1][1] = Gate(Coordinate([0, 10]), ElectroProperty([10, 10]))
        root[1][2] = Gate(Coordinate([0, 50]), ElectroProperty([0, 10]))
        root[1][1][1] = Node(Coordinate([0, 40]))
        root[1][1][1][1] = Gate(Coordinate([0, 40]), ElectroProperty([5, 5]))
        root[1][1][1][2] = Gate(Coordinate([0, 60]), ElectroProperty([0, 5]))
        root[1][1][1][1][1] = Gate(Coordinate([0, 50]), ElectroProperty([0, 5]))

        unit_rc = ElectroProperty([1 / Coordinate.scale] * 2)

        self.assertEqual(DFS(root, unit_rc).delay()[0], 3250)


if __name__ == '__main__':
    unittest.main()
