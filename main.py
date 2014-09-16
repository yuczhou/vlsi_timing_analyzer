import sys
from timer.algorithm.dfs import DFS
from timer.parser.SolutionParser import SolutionParser
from timer.parser.buffer_library_parser import BufferLibraryParser
from timer.parser.net_parser import NetParser

__author__ = 'yuczhou'


def parse_tree_info(files):
    nodes, unit_rc = NetParser(files[2]).parse()
    return SolutionParser(files[0], BufferLibraryParser(files[1]).parse(), nodes).parse(), unit_rc


def main(argv):
    delay, _ = DFS(*parse_tree_info(argv)).delay()
    print delay


if __name__ == '__main__':
    main(sys.argv[1:])