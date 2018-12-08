#!/usr/local/bin/python3

import navsystem

nav = navsystem.NavigationSystem('input.txt')

print('Answer part 1: ' + str(nav.get_metadata_sum()))