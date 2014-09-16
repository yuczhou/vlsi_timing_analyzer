from timer.node.node import Node
from timer.vlsi.electro_property import ElectroProperty

__author__ = 'yuczhou'


class Gate(Node):

    def __init__(self, coord, electro_property=ElectroProperty()):
        Node.__init__(self, coord)
        self._electro_property = electro_property

    def get_capacitor(self, downstream_capacitors):
        return self.electro_property.c