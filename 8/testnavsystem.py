#!/usr/local/bin/python3

import navsystem
import unittest

class test_navsystem(unittest.TestCase):
    def test_metadata(self):
        test_nav = navsystem.NavigationSystem('test.txt')
        self.assertEqual(test_nav.get_metadata_sum(), 138)

if __name__ == '__main__':
    unittest.main()