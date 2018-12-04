#!/usr/local/bin/python3

import guardlog

guard_logger = guardlog.GuardLog('input.txt')
guard_logger.parse_input()
print('Answer: ' + str(guard_logger.get_id_minute()))