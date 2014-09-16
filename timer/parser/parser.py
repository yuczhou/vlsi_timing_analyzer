__author__ = 'yuczhou'
import abc
import os


class Parser(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, file_name):
        self._file_name = os.path.abspath(file_name)
        self._lines = []
        self._nodes = dict()

    @property
    def root(self):
        return self.nodes[0]

    @property
    def nodes(self):
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        self._nodes = nodes

    @property
    def file_name(self):
        return self._file_name

    def lines(self):
        for line in open(self.file_name):
            yield line.strip()

    def split(self, raw):
        return raw.split() if isinstance(raw, str) else raw

    @abc.abstractmethod
    def parse(self):
        pass