from timer.parser.buffer_library_parser import BufferLibraryParser
from timer.vlsi.electro_property import ElectroProperty

__author__ = 'yuczhou'

import unittest


class BufferLibraryParserTest(unittest.TestCase):
    def test_parse_lib(self):
        library = BufferLibraryParser('library.cobalt').parse()
        self.assertEqual(len(library), 10)
        self.assertEqual(library[0], ElectroProperty([1.85, 0.436]))
        self.assertEqual(library[9], ElectroProperty([0.159, 3.5]))


if __name__ == '__main__':
    unittest.main()
