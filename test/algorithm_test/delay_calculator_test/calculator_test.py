from timer.algorithm.delay_calculator.capacitance_calculator import CapacitanceCalculator
from timer.algorithm.delay_calculator.delay_calculator import DelayCalculator
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

        self._unit_rc = ElectroProperty([1 / Coordinate.scale, 1 / Coordinate.scale])

    def test_capacitor_gate(self):
        calculator = CapacitanceCalculator(Gate(Coordinate([1, 1]), ElectroProperty([2, 2])), [2, 3], self._unit_rc)
        self.assertEqual(calculator.calculate(), 2)

    def test_capacitor_node(self):
        calculator = CapacitanceCalculator(self._root_node, [2, 3], self._unit_rc)
        self.assertEqual(calculator.calculate(), 2 + 3 + 1 * 5 + 1 * 6)

    def test_delay_gate(self):
        calculator = DelayCalculator(self._root_gate, [0, 0], [2, 3], self._unit_rc)
        self.assertEqual(calculator.calculate(), 4 * (4 + 5 + 2 + 3) + 5 * (5 / 2.0 + 3))

    def test_delay_node(self):
        calculator = DelayCalculator(self._root_node, [0, 0], [2, 3], self._unit_rc)
        self.assertAlmostEqual(calculator.calculate(), 36)


if __name__ == '__main__':
    unittest.main()
