from abc import ABC, abstractmethod

class GameplayModeStrategy(ABC):
    @abstractmethod
    def play(self):
        pass


class SinglePlayerStrategy(GameplayModeStrategy):
    def play(self):
        print('Playing single player mode...')


class MultiplayerStrategy(GameplayModeStrategy):
    def play(self):
        print('Playing multiplayer mode...')


class OnlineMultiplayerStrategy(GameplayModeStrategy):
    def play(self):
        print('Playing online multiplayer mode...')