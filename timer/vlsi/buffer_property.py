from timer.vlsi.electro_property import ElectroProperty

__author__ = 'yuczhou'


class BufferProperty(ElectroProperty):

    def __init__(self, electro_property=(0, 0), intrinsic_delay=0):
        ElectroProperty.__init__(self, electro_property)
        self._intrinsic_delay = intrinsic_delay

    @property
    def intrinsic_delay(self):
        return self._intrinsic_delay