#!/usr/local/bin/python3

import sys

polymer = ''

with open('input.txt', 'r') as f:
    polymer = f.read().strip('\n')
    #print(polymer)

def get_answer_part_one(polymer):
    i = 0
    while(i < len(polymer)-1):
        reaction_found = False
        if ord(polymer[i]) + 32 == ord(polymer[i+1]) or ord(polymer[i]) == ord(polymer[i+1]) + 32:
            #print(polymer[i] + ' reacts with ' + polymer[i+1])
            polymer = polymer[:i] + polymer[i+2:]
            #print('New polymer: ' +str(polymer))
            reaction_found = True

        if reaction_found:
            i = i - 1
            if i < 0:
                i = 0
        else:
            i = i + 1

    return polymer


def get_answer_part_two(polymer):
    ''' Get length of shortest possible polymer by removing one type '''
    type_to_remove = 65 #ASCII 'A'
    shortest_possible = None
    for j in range(0, 26):
        i = 0
        polymer_j = polymer
        while(i < len(polymer_j)-1):
            reaction_found = False
            if ord(polymer_j[i]) == type_to_remove or ord(polymer_j[i]) == type_to_remove + 32:
                polymer_j = polymer_j[:i] + polymer_j[i+1:]
                reaction_found = True

            if reaction_found:
                i = i - 1
                if i < 0:
                    i = 0
            else:
                i = i + 1

        length = len(get_answer_part_one(polymer_j))
        if shortest_possible is None or length < shortest_possible:
            shortest_possible = length
        type_to_remove = type_to_remove + 1

    return shortest_possible


print('Answer 1: ' + str(len(get_answer_part_one(polymer))))
print('Answer 2: ' + str(get_answer_part_two(polymer)))