from timer.algorithm.algorithm import Algorithm
from timer.algorithm.delay_calculator.calculator import DelayCalculator
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
        worst_delay_list, capacitor_list = zip(*[self._delay(child) for child in root.neighbors()])
        delay_calculator = DelayCalculator(root, capacitor_list, self.electro_property)
        return max([downstream + wire for downstream, wire in
                    zip(worst_delay_list, delay_calculator.worst_delay())]), delay_calculator.capacitance()