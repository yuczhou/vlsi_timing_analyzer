import re
from timer.parser.line_parser.unit_rc_parser import UnitRCParser
from timer.parser.parser import Parser
from timer.vlsi.electro_property import ElectroProperty

__author__ = 'yuczhou'


def is_unit_rc(line):
    return bool(re.compile(r'^(\d+(\.\d*)?|\.\d+)\s+(\d+(\.\d*)?|\.\d+)').match(line))


class WireRCParser(Parser):

    def __init__(self, wire_file):
        Parser.__init__(self, wire_file)

    def parse(self):
        return [UnitRCParser(line).parse() for line in self.lines() if is_unit_rc(line)]
