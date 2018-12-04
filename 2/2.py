#!/usr/local/bin/python3

import checkcount

checker = checkcount.CheckCount('input.txt')
checker.parse_input_file()
checker.print_box_ids()
checker.count_multiple_instances()
print(str(checker.get_number_of_duplicates()))

