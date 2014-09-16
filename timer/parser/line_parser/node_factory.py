from timer.node.gate import Gate

__author__ = 'yuczhou'
import re

from timer.node.node import Node
from timer.coordinate.coordinate import Coordinate as Coord
from timer.vlsi.electro_property import ElectroProperty
from timer.parser.line_parser.line_parser import LineParser


class NodeFactory(LineParser):

    def __init__(self, line):
        LineParser.__init__(self, line)

    def parse(self):
        if is_steiner(self.line) or is_candidate(self.line):
            return self.create_node()
        if is_driver(self.line):
            return self.create_driver()
        if is_sink(self.line):
            return self.create_sink()
        raise TypeError("not a valid node")

    def create_driver(self):
        return self.get_index(), Gate(self.get_coord(), ElectroProperty([float(self.line[4]), 0.0]))

    def create_sink(self):
        return self.get_index(), Gate(self.get_coord(), ElectroProperty([0.0, float(self.line[4])]))

    def create_node(self):
        return self.get_index(), Node(self.get_coord())

    def get_index(self):
        return int(self.line[1])

    def get_coord(self):
        return Coord([int(self.line[2]), int(self.line[3])])


def is_driver(line):
    return bool(re.compile(r'^driver.*$').match(''.join(line)))


def is_sink(line):
    return bool(re.compile(r'^sink.*$').match(''.join(line)))


def is_steiner(line):
    return bool(re.compile(r'^steiner.*$').match(''.join(line)))


def is_candidate(line):
    return bool(re.compile(r'^candidate.*$').match(''.join(line)))