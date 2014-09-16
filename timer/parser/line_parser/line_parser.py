__author__ = 'yuczhou'
import abc


class LineParser(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, line):
        self._line = self.split(line)

    @property
    def line(self):
        return self._line

    @abc.abstractmethod
    def parse(self):
        pass

    def split(self, raw):
        return raw.split() if isinstance(raw, str) else raw