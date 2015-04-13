import abc
from timer.settings import settings

from timer.algorithm.delay_calculator.rc_adjustment import CoordSelector


__author__ = 'yuczhou'


class Calculator(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, root, downstream_capacitor_list, unit_rc, wire_rc_changer):
        self._root = root
        self._downstream_capacitance_list = downstream_capacitor_list
        self._unit_rc = unit_rc
        self._wire_rc_changer = wire_rc_changer

    @property
    def downstream_capacitance_list(self):
        return tuple(self._downstream_capacitance_list)

    @property
    def root(self):
        return self._root

    @property
    def complete_capacitance_list(self):
        return [downstream + wire for downstream, wire in
                zip(self.downstream_capacitance_list, map(lambda _: _.c, self._wire_rc()))]

    def _wire_rc(self):
        return [self._unit_rc * self._wire_rc_adjustment(child) for child in
                self.root.neighbors()]

    def _wire_rc_adjustment(self, child):
        if settings.TEST_MODE:
            return 1
        return sum([random_adjust * actual_length for random_adjust, actual_length in zip(
            [self._wire_rc_changer.get_adjustment(self.root.coord, CoordSelector.LEFT),
             self._wire_rc_changer.get_adjustment(child.coord, CoordSelector.RIGHT)], self.root.distance_from(child))])

    @abc.abstractmethod
    def calculate(self):
        pass