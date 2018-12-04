#!/usr/local/bin/python3

import fabric

santa_fabric = fabric.Fabric('input.txt')
santa_fabric.parse_input()
print('Overlapping inches: ' + str(santa_fabric.get_overlapping_inches()))
santa_fabric.find_non_overlapping_id()