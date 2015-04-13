from timer.algorithm.algorithm import Algorithm
from timer.algorithm.delay_calculator.capacitance_calculator import CapacitanceCalculator
from timer.algorithm.delay_calculator.delay_calculator import DelayCalculator
from timer.node.node import Node

__author__ = 'yuczhou'


class DFS(Algorithm):
    def __init__(self, root, unit_electro_property, rc_adjustment):
        Algorithm.__init__(self, root, unit_electro_property, rc_adjustment)

    def delay(self):
        return self._delay(self.root)

    def _delay(self, root):
        if not isinstance(root, Node):
            raise TypeError('invalid type: Node expected')
        if not root:
            return 0, root.electro_property.c
        downstream_delays, downstream_caps = zip(*[self._delay(child) for child in root.neighbors()])

        delay_cal = DelayCalculator(root, downstream_delays, downstream_caps, self.unit_rc, self.wire_rc_adjustment)
        cap_cal = CapacitanceCalculator(root, downstream_caps, self.unit_rc, self.wire_rc_adjustment)
        return delay_cal.calculate(), cap_cal.calculate()