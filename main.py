import os
import sys
from timer.algorithm.dfs import DFS
from timer.dumper.dumper import Dumper
from timer.parser.solution_parser import SolutionParser
from timer.parser.buffer_library_parser import BufferLibraryParser
from timer.parser.net_parser import NetParser
from timer.parser.variation_parser import VariationParser
from timer.parser.wire_rc_parser import WireRCParser

__author__ = 'yuczhou'

expected_args = ['<buffering solution file>',
                 '<buffer library file>',
                 '<net file>',
                 '<unit rc file>',
                 '<random number file>',
                 '<output delay file>']


def parse(files):
    return SolutionParser(files[0], BufferLibraryParser(files[1]).parse(),
                          NetParser(files[2]).parse()).parse(), WireRCParser(files[3]).parse()


def show_usage():
    print 'Usage: python main.py %s' % ' '.join(expected_args)
    sys.exit(1)


def main(argv):
    if len(argv) != len(expected_args):
        show_usage()

    root, unit_rc_list = parse(argv)
    rc_adjustment = VariationParser(argv[4]).parse()
    Dumper([DFS(root, unit_rc, rc_adjustment).delay()[0] for unit_rc in unit_rc_list], os.path.abspath(argv[5])).dump()
    print 'Worst case calculation succeed! Refer to \'%s\'!\n' % argv[5]


if __name__ == '__main__':
    main(sys.argv[1:])