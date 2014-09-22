__author__ = 'yuczhou'


class Dumper(object):

    def __init__(self, data, file_name='delay.txt'):
        self._data = data if isinstance(data, list) else [data]
        self._file = open(file_name, 'w')

    def dump(self):
        self._file.write('\n'.join(map(str, self._data)))