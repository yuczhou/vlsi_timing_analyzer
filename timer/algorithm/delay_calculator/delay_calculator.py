from timer.algorithm.delay_calculator.calculator import Calculator

__author__ = 'yuczhou'


class DelayCalculator(Calculator):
    def __init__(self, root, down_stream_delay_list, downstream_capacitor_list, unit_rc):
        Calculator.__init__(self, root, downstream_capacitor_list, unit_rc)
        self._downstream_delay_list = down_stream_delay_list

    def _current_delay_list(self):
        return [self._wire_delay(downstream_capacitance, wire_rc) + self._gate_delay() for
                downstream_capacitance, wire_rc in zip(self.downstream_capacitance_list, self._wire_rc())]

    def _wire_delay(self, downstream_capacitance, wire_rc):
        return wire_rc.r * (wire_rc.c / 2.0 + downstream_capacitance)

    def _gate_delay(self):
        return self.root.intrinsic_delay() + self.root.electro_property.r * sum(self.complete_capacitance_list)

    def calculate(self):
        return max([down + current for down, current in zip(self._downstream_delay_list, self._current_delay_list())])