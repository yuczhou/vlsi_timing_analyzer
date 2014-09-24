from timer.parser.line_parser.line_parser import LineParser
from timer.vlsi.electro_property import ElectroProperty

__author__ = 'yuczhou'


class UnitRCParser(LineParser):

    _scaling = 1.0

    def __init__(self, line):
        LineParser.__init__(self, line)

    def parse(self):
        return ElectroProperty(map(lambda _: float(_) * UnitRCParser._scaling, self.line))