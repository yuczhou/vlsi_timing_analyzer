from timer.node.gate import Gate
from timer.vlsi.buffer_property import BufferProperty

__author__ = 'yuczhou'


class Buffer(Gate):

    def __init__(self, coord, electro_property=BufferProperty()):
        Gate.__init__(self, coord, electro_property)

    def intrinsic_delay(self):
        return self.electro_property.intrinsic_delay