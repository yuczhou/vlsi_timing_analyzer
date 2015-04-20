from timer.algorithm.delay_calculator.rc_adjustment import RCAdjustment, CoordSelector
from timer.parser.parser import Parser

__author__ = 'yuczhou'


def get_selector(raw):
    return CoordSelector.LEFT if raw in 'Xx' else CoordSelector.RIGHT


class VariationParser(Parser):
    def __init__(self, variation_file):
        super(VariationParser, self).__init__(variation_file)
        self._rc_adjustment = RCAdjustment()

    @property
    def rc_adjustment(self):
        return self._rc_adjustment

    def parse(self):
        map(self.add_variation, self.lines())
        return self.rc_adjustment

    def add_variation(self, line):
        raw = line.strip().split()
        self.rc_adjustment.set_adjustment(int(float(raw[1])), get_selector(raw[0]), float(raw[2]))
