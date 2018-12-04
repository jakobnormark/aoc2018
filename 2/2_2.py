#!/usr/local/bin/python3

import checkcount

checker = checkcount.CheckCount('input.txt')
checker.parse_input_file()
checker.print_box_ids()
print(str(checker.find_one_char_difference()))

