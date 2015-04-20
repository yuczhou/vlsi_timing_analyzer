import re
from timer import settings
from timer.algorithm.delay_calculator.rc_adjustment import RCAdjustment, CoordSelector
from timer.coordinate.coordinate import Coordinate as Coord

__author__ = 'yuczhou'

import unittest


class RCAdjustmentTest(unittest.TestCase):
    def setUp(self):
        self._adjustment = RCAdjustment()

    def test_single_coord(self):
        self._adjustment.set_adjustment(0, CoordSelector.LEFT, 1.234)
        self.assertEqual(self._adjustment.get_adjustment(0, CoordSelector.LEFT), 1.234)
        self.assertEqual(self._adjustment.get_adjustment(0, CoordSelector.LEFT), 1.234)
        self._adjustment.set_adjustment(1, CoordSelector.LEFT, 2.333)
        self.assertEqual(self._adjustment.get_adjustment(1, CoordSelector.LEFT), 2.333)
        self.assertEqual(self._adjustment.get_adjustment(1, CoordSelector.LEFT), 2.333)

        self._adjustment.set_adjustment(1, CoordSelector.RIGHT, 10.234)
        self.assertEqual(self._adjustment.get_adjustment(1, CoordSelector.RIGHT), 10.234)
        self.assertEqual(self._adjustment.get_adjustment(1, CoordSelector.RIGHT), 10.234)
        self._adjustment.set_adjustment(2, CoordSelector.RIGHT, 20.333)
        self.assertEqual(self._adjustment.get_adjustment(2, CoordSelector.RIGHT), 20.333)
        self.assertEqual(self._adjustment.get_adjustment(2, CoordSelector.RIGHT), 20.333)

    def test_str(self):
        self._adjustment.set_adjustment(0, CoordSelector.LEFT, 1.234)
        self._adjustment.set_adjustment(1, CoordSelector.LEFT, 1.234)
        self._adjustment.set_adjustment(2, CoordSelector.LEFT, 1.234)
        self._adjustment.set_adjustment(1, CoordSelector.RIGHT, 1.234)
        self._adjustment.set_adjustment(2, CoordSelector.RIGHT, 1.234)

        self.assertTrue(bool(re.compile(r'X random numbers:\n(\d \d\.\d+\n)+Y random numbers:\n(\d \d\.\d+\n)+').match(
            str(self._adjustment))))


if __name__ == '__main__':
    unittest.main()
