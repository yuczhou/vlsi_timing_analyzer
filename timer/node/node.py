from timer.vlsi.electro_property import ElectroProperty

__author__ = 'yuczhou'
import abc

from timer.coordinate.coordinate import Coordinate as Coord


class Node(dict):
    """
    Abstract coordinate node
    """
    def __init__(self, coord):
        self._coord = Coord(coord)
        self._electro_property = ElectroProperty()

    @property
    def electro_property(self):
        return self._electro_property

    @property
    def coord(self):
        return self._coord

    def __eq__(self, other):
        return id(self) == id(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def neighbors(self):
        return self.values()

    def distance_from(self, other):
        return self.coord.distance(other.coord)

    def get_capacitor(self, downstream_capacitors):
        return sum(downstream_capacitors)

    def intrinsic_delay(self):
        return 0