from timer.algorithm.delay_calculator.calculator import DelayCalculator
from timer.coordinate.coordinate import Coordinate
from timer.node.gate import Gate
from timer.node.node import Node
from timer.vlsi.electro_property import ElectroProperty

__author__ = 'yuczhou'

import unittest


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self._root_gate = Gate(Coordinate([1, 1]), ElectroProperty([4, 5]))
        self._root_gate[1] = Node(Coordinate([1, 5]))
        self._root_gate[2] = Node(Coordinate([1, 6]))

        self._root_node = Node(Coordinate([1, 0]))
        self._root_node[1] = Node(Coordinate([1, 5]))
        self._root_node[2] = Node(Coordinate([1, 6]))

        self._unit_rc = ElectroProperty([10 / Coordinate.scale, 10 / Coordinate.scale])

        self._delta = 0.0001

    def test_capacitor_gate(self):
        calculator = DelayCalculator(Gate(Coordinate([1, 1]), ElectroProperty([2, 2])), [2, 3], self._unit_rc)
        self.assertEqual(calculator.capacitance(), 2)

    def test_capacitor_node(self):
        calculator = DelayCalculator(self._root_node, [2, 3], self._unit_rc)
        self.assertEqual(calculator.capacitance(), 2 + 3 + 10 * 5 + 10 * 6)

    def test_delay_gate(self):
        calculator = DelayCalculator(self._root_gate, [2, 3], self._unit_rc)
        self.assertEqual(calculator.worst_delay(), max(4 * (40 + 2) + 40 * (20 + 2), 4 * 53 + 50 * 28))

    def test_delay_node(self):
        calculator = DelayCalculator(self._root_node, [2, 3], self._unit_rc)
        self.assertAlmostEqual(calculator.worst_delay(), max(50 * 27, 60 * 33), delta=self._delta)


if __name__ == '__main__':
    unittest.main()
