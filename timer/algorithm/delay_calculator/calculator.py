import abc

__author__ = 'yuczhou'


class Calculator(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, root, downstream_capacitor_list, unit_rc):
        self._root = root
        self._downstream_capacitance_list = downstream_capacitor_list
        self._unit_rc = unit_rc

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
        return [self._unit_rc * self.root.distance_from(child) for child in self.root.neighbors()]

    @abc.abstractmethod
    def calculate(self):
        pass