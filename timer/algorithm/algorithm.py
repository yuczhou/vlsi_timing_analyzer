import abc

__author__ = 'yuczhou'


class Algorithm(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, root, unit_rc):
        self._root = root
        self._unit_rc = unit_rc

    @property
    def root(self):
        return self._root

    @property
    def unit_rc(self):
        return self._unit_rc

    @abc.abstractmethod
    def delay(self):
        pass