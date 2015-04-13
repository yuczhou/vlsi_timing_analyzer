import re
from timer import settings
from timer.algorithm.delay_calculator.rc_adjustment import RCAdjustment, CoordSelector
from timer.coordinate.coordinate import Coordinate as Coord

__author__ = 'yuczhou'

import unittest


class RCAdjustmentTest(unittest.TestCase):
    def setUp(self):
        self._adjustment = RCAdjustment()
        settings.RANDOM_RANGE = (0.8, 1.2)

    def test_single_coord(self):
        adjustment_left = self._adjustment.get_adjustment(Coord([0, 1]), CoordSelector.LEFT)
        self.assertTrue(settings.RANDOM_RANGE[0] <= adjustment_left <= settings.RANDOM_RANGE[1])
        self.assertEqual(self._adjustment.get_adjustment(Coord([0, 1]), CoordSelector.LEFT), adjustment_left)
        self.assertEqual(self._adjustment.get_adjustment(Coord([0, 1]), CoordSelector.LEFT), adjustment_left)

        adjustment_right = self._adjustment.get_adjustment(Coord([0, 1]), CoordSelector.RIGHT)
        self.assertTrue(settings.RANDOM_RANGE[0] <= adjustment_left <= settings.RANDOM_RANGE[1])
        self.assertEqual(self._adjustment.get_adjustment(Coord([0, 1]), CoordSelector.RIGHT), adjustment_right)
        self.assertEqual(self._adjustment.get_adjustment(Coord([0, 1]), CoordSelector.RIGHT), adjustment_right)

        self.assertNotEqual(adjustment_left, adjustment_right)

    def test_multiple_coord(self):
        sample_size = 10
        self.assertEqual(len(
            set([self._adjustment.get_adjustment(Coord([i, i]), CoordSelector.LEFT) for i in xrange(0, sample_size)])),
            sample_size)

    def test_str(self):
        self._adjustment.get_adjustment(Coord([0, 0]), CoordSelector.LEFT)
        self._adjustment.get_adjustment(Coord([1, 0]), CoordSelector.LEFT)
        self._adjustment.get_adjustment(Coord([2, 0]), CoordSelector.LEFT)
        self._adjustment.get_adjustment(Coord([0, 0]), CoordSelector.RIGHT)
        self._adjustment.get_adjustment(Coord([0, 1]), CoordSelector.RIGHT)
        self.assertTrue(bool(re.compile(r'X random numbers:\n(\d \d\.\d+\n)+Y random numbers:\n(\d \d\.\d+\n)+').match(
            str(self._adjustment))))


if __name__ == '__main__':
    unittest.main()
