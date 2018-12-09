#!/usr/local/bin/python3

import marblegame

mg = marblegame.MarbleGame(464, 70918)

print('Answer part 1: ' + str(mg.get_winning_score()))

mg_two = marblegame.MarbleGame(464, 7091800)
print('Answer part 1: ' + str(mg_two.get_winning_score()))