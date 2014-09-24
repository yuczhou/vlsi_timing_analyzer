__author__ = 'yuczhou'


class DelayCalculator(object):
    def __init__(self, root, downstream_capacitor_list, unit_rc):
        self._root = root
        self._downstream_capacitor_list = downstream_capacitor_list
        self._unit_rc = unit_rc

    @property
    def downstream_capacitor_list(self):
        return tuple(self._downstream_capacitor_list)

    @property
    def root(self):
        return self._root

    def _wire_rc(self):
        return [self._wire_rc_single(child) for child in self.root.neighbors()]

    def _wire_rc_single(self, child):
        return self._unit_rc * self.root.distance_from(child)

    def worst_delay(self):
        return [self._single_delay(downstream_capacitor, wire_rc) for downstream_capacitor, wire_rc in
                zip(self.downstream_capacitor_list, self._wire_rc())]

    def _single_delay(self, downstream_capacitor, wire_rc):
        return self.root.intrinsic_delay() + self.root.electro_property.r * (
            wire_rc.c + downstream_capacitor) + wire_rc.r * (wire_rc.c / 2.0 + downstream_capacitor)

    def capacitance(self):
        return self.root.get_capacitor(self._capacitance_list)

    @property
    def _capacitance_list(self):
        return [downstream + wire for downstream, wire in
                zip(self.downstream_capacitor_list, map(lambda _: _.c, self._wire_rc()))]