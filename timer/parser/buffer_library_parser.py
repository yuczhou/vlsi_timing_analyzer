import re
from timer.parser.parser import Parser
from timer.vlsi.buffer_property import BufferProperty

__author__ = 'yuczhou'


class BufferLibraryParser(Parser):
    def __init__(self, library_file):
        Parser.__init__(self, library_file)
        self._buffer_list = []

    @property
    def buffer_list(self):
        return self._buffer_list

    def parse(self):
        self._buffer_list = [BufferProperty([r, c], intrinsic_delay) for r, c, intrinsic_delay in
                             zip(self._extract_info(self.is_resistance), self._extract_info(self.is_input_capacitance),
                                 self._extract_info(self.is_intrinsic_delay))]
        return self.buffer_list

    def _extract_info(self, filter_func):
        return map(lambda line: float(self.split(line)[1]), filter(filter_func, self.lines()))

    def is_input_capacitance(self, line):
        return bool(re.compile(r'^inputCap.*$').match(line))

    def is_resistance(self, line):
        return bool(re.compile(r'^resistance.*$').match(line))

    def is_intrinsic_delay(self, line):
        return bool(re.compile(r'^intrinsicDelay.*$').match(line))