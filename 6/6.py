#!/usr/local/bin/python3

import coordinator

coord = coordinator.Coordinator('input.txt')
coord.populate_manhattan_distances()

print('Answer part 1: ' + str(coord.get_size_of_largest_area_not_infinite()))