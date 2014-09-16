__author__ = 'yuczhou'


class ElectroProperty(object):

    def __init__(self, electro_property=(0, 0)):
        self._electro_property = electro_property

    @property
    def r(self):
        return self._electro_property[0]

    @property
    def c(self):
        return self._electro_property[1]

    def __eq__(self, other):
        return self.r == other.r and self.c == other.c

    def __ne__(self, other):
        return self != other

    def __mul__(self, wire_length):
        return ElectroProperty([self.r * wire_length, self.c * wire_length])