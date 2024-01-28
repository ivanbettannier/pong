
class Game_stats:
    """Follow score of the game"""

    def __init__(self, pong):
        """Initialize settings"""
        self.settings = pong.settings
        self.player1_point = 0
        self.player2_point = 0
        self.increment_score = False

    def count_point(self, player):
        if self.increment_score:
            if player == 1:
                self.player1_point += 1
            if player == 2:
                self.player2_point += 1
        self.increment_score = False



    

    