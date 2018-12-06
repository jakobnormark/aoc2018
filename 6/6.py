#!/usr/local/bin/python3

import coordinator

coord = coordinator.Coordinator('input.txt')

print('Answer part 2: ' + str(coord.get_manhattan_region(10000)))

coord.populate_manhattan_distances()

print('Answer part 1: ' + str(coord.get_size_of_largest_area_not_infinite()))