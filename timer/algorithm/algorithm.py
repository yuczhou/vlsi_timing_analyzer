import abc
from timer.algorithm.delay_calculator.rc_adjustment import RCAdjustment

__author__ = 'yuczhou'


class Algorithm(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, root, unit_rc, wire_rc_adjustment):
        self._root = root
        self._unit_rc = unit_rc
        self._wire_rc_adjustment = wire_rc_adjustment

    @property
    def root(self):
        return self._root

    @property
    def unit_rc(self):
        return self._unit_rc

    @property
    def wire_rc_adjustment(self):
        return self._wire_rc_adjustment

    @abc.abstractmethod
    def delay(self):
        pass