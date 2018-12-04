#!/usr/local/bin/python3

import guardlog

guard_logger = guardlog.GuardLog('input.txt')
guard_logger.parse_input()
print('Answer part 1: ' + str(guard_logger.get_id_minute()))

print('Answer part 2: ' + str(guard_logger.get_id_minute_most_frequent()))