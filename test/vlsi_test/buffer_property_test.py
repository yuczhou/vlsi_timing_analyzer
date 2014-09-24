from timer.vlsi.buffer_property import BufferProperty

__author__ = 'yuczhou'

import unittest


class BufferPropertyTest(unittest.TestCase):

    def test_constructor(self):
        electro_property = BufferProperty([1, 2], 5)
        self.assertEqual(electro_property.intrinsic_delay, 5)
        self.assertEqual(electro_property.r, 1)
        self.assertEqual(electro_property.c, 2)

    def test_equals(self):
        self.assertEqual(BufferProperty([1, 2], 5), BufferProperty([1, 2], 5))
        self.assertNotEqual(BufferProperty([1, 2], 0), BufferProperty([1, 2], 5))


if __name__ == '__main__':
    unittest.main()
