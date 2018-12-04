#!/usr/local/bin/python3

import collections

''' Advent of code 2018-12-02 '''

class CheckCount:
    def __init__(self, file_name):
        self.file_name = file_name
        self.box_ids = []
        self.doubles = 0
        self.triples = 0

    def parse_input_file(self):
        ''' Parse input file and store box IDs in set '''
        with open(self.file_name, 'r') as f:
            rows = f.readlines()
            for line in rows:
                to_add = [] 
                letters = line.strip('\n')
                for letter in letters:
                    to_add.append(letter)
                self.box_ids.append(to_add)
                print('Appended : ' + str(to_add))
        self.box_ids.sort()
        print(str(self.box_ids))

    def count_multiple_instances(self):
        for box_id in self.box_ids:
            counter=collections.Counter(box_id)
            if 2 in counter.values():
                #print('Double!')
                #print(str(counter.values()))
                self.doubles = self.doubles + 1
            if 3 in counter.values():
                #print('Triple!')
                #print(str(counter.values()))
                self.triples = self.triples + 1

    def get_number_of_duplicates(self):
        return self.doubles * self.triples

    def find_one_char_difference(self):
        for box_id in self.box_ids:
            box_stripped = self.box_ids
            box_stripped.remove(box_id)
            for box in box_stripped:
                i = 0
                difference = 0
                code = []
                for letter in box_id:
                    if letter != box[i]:
                        difference = difference + 1
                    else:
                        code.append(letter)
                    i = i + 1
                if difference == 1:
                    print((''.join(code)))
                    

    def print_box_ids(self):
        print(str(self.box_ids))
