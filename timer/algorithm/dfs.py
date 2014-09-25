from timer.algorithm.algorithm import Algorithm
from timer.algorithm.delay_calculator.capacitance_calculator import CapacitanceCalculator
from timer.algorithm.delay_calculator.delay_calculator import DelayCalculator
from timer.node.node import Node

__author__ = 'yuczhou'


class DFS(Algorithm):
    def __init__(self, root, unit_electro_property):
        Algorithm.__init__(self, root, unit_electro_property)

    def delay(self):
        return self._delay(self.root)

    def _delay(self, root):
        if not isinstance(root, Node):
            raise TypeError('invalid type: Node expected')
        if not root:
            return 0, root.electro_property.c
        downstream_delay_list, downstream_capacitance_list = zip(*[self._delay(child) for child in root.neighbors()])
        return DelayCalculator(root, downstream_delay_list, downstream_capacitance_list, self.unit_rc).calculate(),\
               CapacitanceCalculator(root, downstream_capacitance_list, self.unit_rc).calculate()