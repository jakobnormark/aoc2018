#!/usr/local/bin/python3

import unittest
import fabric

class TestFabric(unittest.TestCase):
    def test_parse_input(self):
        testfabric = fabric.Fabric('test.txt')
        #testfabric = fabric.Fabric('input.txt')
        testfabric.parse_input()
        self.assertEqual(testfabric.get_overlapping_inches(), 4)

if __name__ == '__main__':
    unittest.main()