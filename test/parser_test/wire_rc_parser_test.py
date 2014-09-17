from timer.parser.wire_rc_parser import WireRCParser
from timer.vlsi.electro_property import ElectroProperty

__author__ = 'yuczhou'

import unittest


class WireRCParserTest(unittest.TestCase):
    def test_complete(self):
        self.assertEqual(len(WireRCParser('cnt_res_cap_5000.txt').parse()), 5000)

    def test_content(self):
        self.assertIn(ElectroProperty([0.006499, 0.142514]), WireRCParser('cnt_res_cap_5000.txt').parse())


if __name__ == '__main__':
    unittest.main()
