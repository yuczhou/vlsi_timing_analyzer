from timer.parser.line_parser.line_parser import LineParser

__author__ = 'yuczhou'


class SolutionLineParser(LineParser):

    def __init__(self, line):
        LineParser.__init__(self, line)

    def parse(self):
        return int(self.line[1]), int(self.line[3]), int(self.line[5])