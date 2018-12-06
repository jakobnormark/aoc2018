#!/usr/local/bin/python3

import coordinator
import unittest

class test_coordinator(unittest.TestCase):
    def test_parser(self):
        test_coord = coordinator.Coordinator('test.txt')
        self.assertEqual(test_coord.get_manhattan_region(32), 16)
        test_coord.populate_manhattan_distances()
        self.assertEqual(test_coord.get_size_of_largest_area_not_infinite(), 17)


if __name__ == '__main__':
    unittest.main()