from timer.vlsi.electro_property import ElectroProperty

__author__ = 'yuczhou'

import re

from timer.parser.parser import Parser
from timer.parser.line_parser.node_factory import NodeFactory


class NetParser(Parser):
    def __init__(self, netfile):
        Parser.__init__(self, netfile)
        self._unit_electro_property = None

    def root(self):
        return self.nodes[0]

    @property
    def unit_electro_property(self):
        return self._unit_electro_property

    def parse(self):
        map(self.create_node, [line.split() for line in self.lines()])
        self._unit_electro_property = ElectroProperty(
            [self._parse_unit_rc(is_valid_wire_unit_res), self._parse_unit_rc(is_valid_wire_unit_cap)])
        map(self.create_edge, filter(is_edge, self.lines()))
        return self.nodes, self.unit_electro_property

    def _parse_unit_rc(self, filter_func):
        return float(self.split(filter(filter_func, self.lines())[0])[1])

    def create_edge(self, raw):
        splitted = self.split(raw)
        self._nodes[int(splitted[1])][int(splitted[2])] = self._nodes[int(splitted[2])]

    def create_node(self, raw):
        try:
            index, node = NodeFactory(raw).parse()
            self._nodes[index] = node
        except TypeError:
            pass


def is_valid_wire_unit_res(line):
    return bool(re.compile(r'^wire_res_per_unit_length.*$').match(line))


def is_valid_wire_unit_cap(line):
    return bool(re.compile(r'^wire_cap_per_unit_length.*$').match(line))


def is_edge(line):
    return bool(re.compile(r'^edge.*$').match(line))