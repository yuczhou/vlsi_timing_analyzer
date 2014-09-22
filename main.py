import os
import sys
from timer.algorithm.dfs import DFS
from timer.dumper.dumper import Dumper
from timer.parser.solution_parser import SolutionParser
from timer.parser.buffer_library_parser import BufferLibraryParser
from timer.parser.net_parser import NetParser
from timer.parser.wire_rc_parser import WireRCParser

__author__ = 'yuczhou'


def parse(files):
    return SolutionParser(files[0], BufferLibraryParser(files[1]).parse(),
                          NetParser(files[2]).parse()).parse(), WireRCParser(files[3]).parse()


def main(argv):
    root, unit_rc_list = parse(argv)
    Dumper([DFS(root, unit_rc).delay()[0] for unit_rc in unit_rc_list], os.path.abspath(argv[4])).dump()
    print 'Worst case calculation succeed! Refer to \'%s\' in current directory!' % argv[4]


if __name__ == '__main__':
    main(sys.argv[1:])