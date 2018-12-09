#!/usr/local/bin/python3

import marblegame
import unittest

class test_marblegame(unittest.TestCase):
    def test_ten_players(self):
        test_mg = marblegame.MarbleGame(10, 25)
        self.assertEqual(test_mg.get_winning_score(), 32)

    def test_1618_marbles(self):
        test_mg = marblegame.MarbleGame(10, 1618)
        self.assertEqual(test_mg.get_winning_score(), 8317)

    def test_13_players(self):
        test_mg = marblegame.MarbleGame(13, 7999)
        self.assertEqual(test_mg.get_winning_score(), 146373)
        
    def test_17_players(self):
        test_mg = marblegame.MarbleGame(17, 1104)
        self.assertEqual(test_mg.get_winning_score(), 2764)

    def test_21_players(self):
        test_mg = marblegame.MarbleGame(21, 6111)
        self.assertEqual(test_mg.get_winning_score(), 54718)

    def test_30_players(self):
        test_mg = marblegame.MarbleGame(30, 5807)
        self.assertEqual(test_mg.get_winning_score(), 37305)

if __name__ == '__main__':
    unittest.main()