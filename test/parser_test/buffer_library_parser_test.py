from timer.parser.buffer_library_parser import BufferLibraryParser
from timer.vlsi.buffer_property import BufferProperty

__author__ = 'yuczhou'

import unittest


class BufferLibraryParserTest(unittest.TestCase):
    def test_parse_lib(self):
        library = BufferLibraryParser('library.cobalt').parse()
        self.assertEqual(len(library), 10)
        self.assertEqual(library[0], BufferProperty([1.85, 0.436], 0.59))
        self.assertEqual(library[9], BufferProperty([0.159, 3.5], 2.87))


if __name__ == '__main__':
    unittest.main()
