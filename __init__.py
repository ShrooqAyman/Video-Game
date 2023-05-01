from facade import GameModeFacade


if __name__ == "__main__":
    game_mode = GameModeFacade()

    game_mode.selectSinglePlayer()
    game_mode.play() # Output: Playing single player mode...

    game_mode.selectMultiplayer()
    game_mode.play() # Output: Playing multiplayer mode...

    game_mode.selectOnlineMultiplayer()
    game_mode.play() # Output: Playing online multiplayer mode...
