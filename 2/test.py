#!/usr/local/bin/python3

import unittest
import checkcount

class TestCheckCount(unittest.TestCase):
    def test_parse_print(self):
        checker = checkcount.CheckCount('test.txt')
        checker.parse_input_file()
        checker.print_box_ids()
        checker.count_multiple_instances()
        self.assertEqual(checker.get_number_of_duplicates(), 12)

    def test_diff_charachters(self):
        checker = checkcount.CheckCount('test2.txt')
        checker.parse_input_file()
        checker.find_one_char_difference()

if __name__ == '__main__':
    unittest.main()
