from timer.parser.solution_parser import SolutionParser
from timer.parser.buffer_library_parser import BufferLibraryParser
from timer.parser.net_parser import NetParser

__author__ = 'yuczhou'

import unittest


class SolutionParserTest(unittest.TestCase):
    def setUp(self):
        self._parser = SolutionParser('buffersolution_net0.txt', BufferLibraryParser('library.cobalt').parse(),
                                      NetParser('0.net').parse())

    def test_buffer(self):
        org_neighbors = self._neighbors(63)
        self._parser.parse()
        self.assertNotEqual(org_neighbors, self._neighbors(63))
        self.assertEqual(len(filter(lambda _: _ not in org_neighbors, self._neighbors(63))), 1)
        self.assertEqual(len(filter(lambda _: _ not in org_neighbors, self._neighbors(63))[0]), 1)

    def _neighbors(self, node_index):
        return self._parser.nodes[node_index].neighbors()[:]


if __name__ == '__main__':
    unittest.main()
