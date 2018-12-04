#!/usr/local/bin/python3

import bisect
import sys

''' Advent of code 2018-12-01 '''

class Sequence:
    def __init__(self):
        self.frequencies = []
        self.frequency_list = [0]

    def adjust_frequency(self, frequency, adjustment):
        ''' Adjust the given frequency with given adjustment '''
        frequency = frequency + adjustment
        self.insert_frequency(frequency)
        #print('New frequency: ' + str(frequency))
        return frequency

    def process_adjustments(self):
        ''' Process adjustments and return frequency '''
        adjusted = 0
        while len(self.frequencies) > 0:
            for adjustment in self.frequencies:
                adjusted = self.adjust_frequency(adjusted, adjustment)

        print('Adjusted frequency: ' + str(adjusted))

    def insert_frequency(self, new_frequency):
        ''' Insert and find first duplicate frequency '''
        #print('Inserting ' + str(new_frequency))
        #print(str(len(self.frequency_list)))
        #print('Frequency list: ' + str(self.frequency_list))
        position = 0
        if len(self.frequency_list) > 0:
            position = bisect.bisect_left(self.frequency_list, new_frequency)
            #print('Got position ' + str(position))
            if position >= len(self.frequency_list):
                pass
            elif position == len(self.frequency_list)-1:
                if self.frequency_list[position] != new_frequency:
                    pass
                else:
                    print('Found duplicate: ' + str(new_frequency))
                    sys.exit(0)
            elif self.frequency_list[position] == new_frequency:
                print('Found duplicate: ' + str(new_frequency))
                sys.exit(0)
            self.frequency_list.insert(position, new_frequency)
        else:
            self.frequency_list.append(new_frequency)
        #print('Appended ' + str(new_frequency))

    def set_frequencies(self, new_frequencies):
        self.frequencies = new_frequencies

    def parse_input_file(self):
        frequencies = []
        with open('1_input.txt', 'r') as f:
            rows = f.readlines()
            for line in rows:
                frequencies.append(int(str(line)))

        print(frequencies)
        self.frequencies = frequencies

