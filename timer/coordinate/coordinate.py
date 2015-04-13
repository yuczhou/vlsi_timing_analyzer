__author__ = 'yuczhou'


class Coordinate(object):

    scale = 1 / 5000.0
    
    def __init__(self, coord):
        self._coord = coord if hasattr(coord, "__iter__") else coord.coord
        
    @property
    def coord(self):
        return self._coord
    
    def __len__(self):
        return sum([abs(_) for _ in self.coord])

    def __eq__(self, other):
        return self.coord == other.coord

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return str(self.coord)

    def distance(self, coordinate):
        return [abs(c1 - c2) * Coordinate.scale for c1, c2 in zip(self.coord, coordinate.coord)]
