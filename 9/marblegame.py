import sys

class MarbleGame():
    def __init__(self, number_of_players, number_of_marbles):
        self.number_of_players = number_of_players
        self.number_of_marbles = number_of_marbles
        self.marbles = []
        self.player_scores = [0 for x in range(0, number_of_players)]

    def get_winning_score(self):
        ''' Get the score for the winning elf '''
        high_score = 0
        current_marble = 0
        current_player = 0
        self.marbles.append(0)

        # For each marble
        for i in range(1, self.number_of_marbles+1):
            if i % 23 == 0 and i != 0:
                # Marbles that are multiples of 23 adds to the current players score
                marble_to_pop = 0
                if current_marble < 7:
                    # Handle wrapping counter-clockwise
                    offset = 7 - current_marble
                    marble_to_pop = len(self.marbles) - offset
                else:
                    marble_to_pop = current_marble-7
                popped = self.marbles.pop(marble_to_pop)
                score = i + popped
                self.player_scores[current_player] = self.player_scores[current_player] + score
                current_marble = marble_to_pop

            else:
                # Insert the new marble
                new_index = current_marble + 1
                for j in range(0,1):
                    if new_index >= len(self.marbles):
                        new_index = 0
                    new_index = new_index + 1
                self.marbles.insert(new_index, i)
                current_marble = new_index

            current_player = current_player + 1
            if current_player >= len(self.player_scores):
                current_player = 0

            if i % 1000000 == 0:
                print('Progress')
        
        for player_score in self.player_scores:
            if player_score > high_score:
                high_score = player_score

        return high_score