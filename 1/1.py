#!/usr/local/bin/python3


''' Advent of code 2018-12-01 '''

def adjust_frequency(frequency, adjustment):
    ''' Adjust the given frequency with given adjustment '''
    frequency = frequency + adjustment
    #print('New frequency: ' + str(frequency))
    return frequency

def process_adjustments(adjustment_list):
    ''' Process adjustments and return frequency '''
    adjusted = 0
    for adjustment in adjustment_list:
        adjusted = adjust_frequency(adjusted, adjustment)

    print('Adjusted frequency: ' + str(adjusted))

def parse_input_file():
    frequencies = []
    with open('1_input.txt', 'r') as f:
        rows = f.readlines()
        for line in rows:
            frequencies.append(int(str(line)))

    print(frequencies)
    return frequencies

adjustments = [1, -2, 3, 1]
process_adjustments(adjustments)
adjustments = [1, 1, 1]
process_adjustments(adjustments)
adjustments = [1, 1, -2]
process_adjustments(adjustments)
adjustments = [-1, -2, -3]
process_adjustments(adjustments)

print('Parsing file and processing input frequencies')
adjustments = parse_input_file()
process_adjustments(adjustments)
