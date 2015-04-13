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


    def get_adjustment(self, coord, selector):
        if not isinstance(coord, Coord):
            raise TypeError('invalid type')
        if not coord.coord[selector] in self._adjustment[selector]:
            random_range = settings.RANDOM_RANGE
            self._adjustment[selector][coord.coord[selector]] = random.uniform(random_range[0], random_range[1])
        return self._adjustment[selector][coord.coord[selector]]
