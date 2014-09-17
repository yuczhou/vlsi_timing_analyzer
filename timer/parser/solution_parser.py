import re
from timer.node.gate import Gate
from timer.parser.line_parser.buffer_solution import SolutionLineParser
from timer.parser.parser import Parser

__author__ = 'yuczhou'


class SolutionParser(Parser):

    def __init__(self, solution_file, buffer_library, nodes):
        Parser.__init__(self, solution_file)
        self._buffer_library = buffer_library
        self.nodes = nodes

    def parse(self):
        map(self.add_buffer, filter(self.is_buffer, self.lines()))
        return self.root

    def add_buffer(self, line):
        start, end, buffer_type = SolutionLineParser(line).parse()
        new_buffer = Gate(self.nodes[start].coord, self._buffer_library[buffer_type])
        new_buffer[end] = self.nodes[end]
        self.nodes[start][id(new_buffer)] = new_buffer
        del self.nodes[start][end]

    def is_buffer(self, line):
        return bool(re.compile(r'^start.*end.*buffertype.*').match(line))