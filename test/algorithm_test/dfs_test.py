from timer.algorithm.delay_calculator.rc_adjustment import RCAdjustment
from timer.algorithm.dfs import DFS
from timer.coordinate.coordinate import Coordinate
from timer.node.buffer import Buffer
from timer.node.gate import Gate
from timer.node.node import Node
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
        self.assertEqual(DFS(self._root_gate, self._unit_rc, RCAdjustment()).delay()[0], 324.5)

    def test_simple_no_buffer(self):
        root = Gate(Coordinate([0, 0]), ElectroProperty([10, 0]))
        root[1] = Gate(Coordinate([10, 0]), ElectroProperty([0, 5]))

        unit_rc = ElectroProperty([1 / Coordinate.scale] * 2)

        self.assertEqual(DFS(root, unit_rc, RCAdjustment()).delay()[0], 250)

    def test_simple_one_buffer(self):
        root = Gate(Coordinate([0, 0]), ElectroProperty([10, 0]))
        root[1] = Buffer(Coordinate([0, 0]), BufferProperty([10, 10], 0))
        root[1][1] = Gate(Coordinate([10, 0]), ElectroProperty([0, 5]))

        unit_rc = ElectroProperty([1 / Coordinate.scale] * 2)

        self.assertEqual(DFS(root, unit_rc, RCAdjustment()).delay()[0], 350)

    def test_two_branch_one_buffer(self):
        root = Gate(Coordinate([0, 0]), ElectroProperty([10, 0]))
        root[1] = Node(Coordinate([5, 0]))
        root[1][1] = Gate(Coordinate([5, 0]), ElectroProperty([10, 10]))
        root[1][1][1] = Gate(Coordinate([10, 0]), ElectroProperty([0, 5]))
        root[1][2] = Gate(Coordinate([10, 5]), ElectroProperty([0, 10]))

        unit_rc = ElectroProperty([1 / Coordinate.scale] * 2)

        self.assertEqual(DFS(root, unit_rc, RCAdjustment()).delay()[0], 662.5)

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

        self.assertEqual(DFS(root, unit_rc, RCAdjustment()).delay()[0], 3250)

    def test_binary_tree(self):
        driver_0 = Gate(Coordinate([0, 0]), ElectroProperty([1, 0]))
        buffer_1 = Gate(Coordinate([6, 0]), ElectroProperty([2, 2]))
        node_2 = Node(Coordinate([6, 0]))
        buffer_3 = Gate(Coordinate([6, 0]), ElectroProperty([5, 5]))
        sink_4 = Gate(Coordinate([26, 0]), ElectroProperty([0, 10]))
        sink_5 = Gate(Coordinate([16, 0]), ElectroProperty([0, 10]))
        node_6 = Node(Coordinate([0, 10]))
        sink_7 = Gate(Coordinate([0, 20]), ElectroProperty([0, 5]))
        buffer_8 = Gate(Coordinate([0, 10]), ElectroProperty([4, 4]))
        sink_9 = Gate(Coordinate([0, 16]), ElectroProperty([0, 10]))

        driver_0[1] = buffer_1
        buffer_1[2] = node_2
        node_2[3] = buffer_3
        buffer_3[4] = sink_4
        node_2[5] = sink_5
        driver_0[6] = node_6
        node_6[7] = sink_7
        node_6[8] = buffer_8
        buffer_8[9] = sink_9

        unit_rc = ElectroProperty([1 / Coordinate.scale] * 2)

        self.assertEqual(DFS(driver_0, unit_rc, RCAdjustment()).delay()[0], 667)


if __name__ == '__main__':
    unittest.main()
