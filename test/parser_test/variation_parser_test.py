from timer.algorithm.delay_calculator.rc_adjustment import CoordSelector
from timer.parser.variation_parser import VariationParser

__author__ = 'yuczhou'

import unittest


class VariationParserTest(unittest.TestCase):
    def setUp(self):
        self._parser = VariationParser('variation.txt')

    def test_parsing(self):
        rc_adjustment = self._parser.parse()
        self.assertEqual(0.9, rc_adjustment.get_adjustment(200, CoordSelector.LEFT))
        self.assertEqual(0.8, rc_adjustment.get_adjustment(100, CoordSelector.LEFT))
        self.assertEqual(1.1, rc_adjustment.get_adjustment(50, CoordSelector.RIGHT))
        self.assertEqual(0.85, rc_adjustment.get_adjustment(150, CoordSelector.LEFT))
        self.assertEqual(0.85, rc_adjustment.get_adjustment(300, CoordSelector.RIGHT))


if __name__ == '__main__':
    unittest.main()
