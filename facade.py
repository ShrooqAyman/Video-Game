from GameplayModeContext import GameplayModeContext
from GameplayModeStrategy import SinglePlayerStrategy, OnlineMultiplayerStrategy, MultiplayerStrategy

class GameModeFacade:
    def __init__(self):
        self.GameplayModeContext = GameplayModeContext(SinglePlayerStrategy())

    
    def selectSinglePlayer(self):
        self.GameplayModeContext.set_strategy(SinglePlayerStrategy())


    def selectMultiplayer(self):
        self.GameplayModeContext.set_strategy(MultiplayerStrategy())

        
    def selectOnlineMultiplayer(self) :
        self.GameplayModeContext.set_strategy(OnlineMultiplayerStrategy())


    def play(self):
        self.GameplayModeContext.play()
        