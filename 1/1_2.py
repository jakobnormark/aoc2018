#!/usr/local/bin/python3
import sequence

''' Advent of code 2018-12-01 '''

print('Test 1')
test_one = sequence.Sequence()
#test_one.set_frequencies([1, -1])
#test_one.set_frequencies([-6, 3, 8, 5, -6])
#test_one.set_frequencies([3, 3, 4, -2, -4])
#test_one.set_frequencies([7, 7, -2, -7, -4])
#test_one.process_adjustments()

print('Parsing file and processing input frequencies')
seq = sequence.Sequence()
seq.parse_input_file()
seq.process_adjustments()

# 1 0
