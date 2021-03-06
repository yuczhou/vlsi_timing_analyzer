from timer.algorithm.delay_calculator.calculator import Calculator

__author__ = 'yuczhou'


class CapacitanceCalculator(Calculator):
    def __init__(self, root, downstream_capacitor_list, unit_rc, wire_rc_changer):
        Calculator.__init__(self, root, downstream_capacitor_list, unit_rc, wire_rc_changer)

    def calculate(self):
        return self.root.get_capacitor(self.complete_capacitance_list)