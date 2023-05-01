from GameplayModeStrategy import SinglePlayerStrategy, MultiplayerStrategy, OnlineMultiplayerStrategy

class GameplayModeContext:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy =strategy

    def play(self):
        self.strategy.play()

       