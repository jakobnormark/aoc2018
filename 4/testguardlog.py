#!/usr/local/bin/python3

import unittest
import guardlog

class TestFabric(unittest.TestCase):
    def test_get_minutes_slept(self):
        testgl = guardlog.GuardLog('test.txt')
        testgl.parse_input()
        # Verify that guard 10 slept 50 minutes
        self.assertEqual(sum(testgl.get_sleep_array(10)), 50)

    def test_get_minutes_slept(self):
        testgl = guardlog.GuardLog('test.txt')
        testgl.parse_input()

        # Verify that test input renders the answer 240
        self.assertEqual(testgl.get_id_minute(), 240)

    def test_get_most_frequent(self):
        testgl = guardlog.GuardLog('test.txt')
        testgl.parse_input()
        self.assertEqual(testgl.get_id_minute_most_frequent(), 4455)

if __name__ == '__main__':
    unittest.main()