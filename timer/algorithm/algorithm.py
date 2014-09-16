import abc

__author__ = 'yuczhou'


class Algorithm(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, root, rc):
        self._root = root
        self._electro_property = rc

    @property
    def root(self):
        return self._root

    @property
    def electro_property(self):
        return self._electro_property

    @abc.abstractmethod
    def delay(self):
        pass