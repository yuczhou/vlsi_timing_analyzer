import random
from timer.coordinate.coordinate import Coordinate as Coord
from timer.settings import Enum, settings

__author__ = 'yuczhou'

CoordSelector = Enum({"LEFT": 0, "RIGHT": 1})


class RCAdjustment(object):
    def __init__(self):
        self._adjustment = [dict(), dict()]
        random.seed(0)

    def __str__(self):
        return "X random numbers:\n" + self._single_dict_str(
            CoordSelector.LEFT) + "\nY random numbers:\n" + self._single_dict_str(CoordSelector.RIGHT)

    def _single_dict_str(self, selector):
        return "\n".join([str(key) + " " + str(value) for key, value in self._adjustment[selector].iteritems()])

    def set_adjustment(self, key, selector, value):
        if not isinstance(key, int):
            raise TypeError('invalid type')
        if key in self._adjustment[selector]:
            raise RuntimeError('Key %s already has random value assigned!' % str(key))
        self._adjustment[selector][key] = value

    def get_adjustment(self, key, selector):
        if not isinstance(key, int):
            raise TypeError('invalid type')
        if key not in self._adjustment[selector]:
            raise RuntimeError('Key %s has no random value assigned!' % str(key))
        return self._adjustment[selector][key]
