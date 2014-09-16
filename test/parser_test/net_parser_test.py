from timer.coordinate.coordinate import Coordinate

__author__ = 'yuczhou'

import unittest

from timer.parser.net_parser import NetParser
from timer.vlsi.electro_property import ElectroProperty


class NetParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = NetParser('0.net')
        self.node_num = 172

    def test_node(self):
        self.parser.parse()
        for node in xrange(self.node_num):
            self.assertIn(node, self.parser.nodes)

    def test_electro_property(self):
        self.parser.parse()
        self.assertEqual(self.parser.nodes[0].electro_property, ElectroProperty([0.328886, 0]))
        self.assertEqual(self.parser.nodes[6].electro_property, ElectroProperty([0, 0.004111]))

    def test_coordinate(self):
        self.parser.parse()
        self.assertEqual(self.parser.nodes[0].coord, Coordinate([8022000, 1631840]))
        self.assertEqual(self.parser.nodes[9].coord, Coordinate([11246480, 6372240]))
        self.assertEqual(self.parser.nodes[1].coord, Coordinate([10490480, 1631840]))
        self.assertEqual(self.parser.nodes[3].coord, Coordinate([2247280, 1631840]))

    def test_edge(self):
        self.parser.parse()
        self.assertIn(171, self.parser.nodes[43])
        self.assertNotIn(170, self.parser.nodes[43])
        self.assertIn(21, self.parser.nodes[10])


if __name__ == '__main__':
    unittest.main()