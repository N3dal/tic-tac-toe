"""
    all the tools and the defaults needed for the game to work;

"""

from os import name as OS_NAME
from os import system


class Tools:
    """"""

    # the file that we will use to save our status;
    DEFAULT_FILE_NAME = "last_game_data.json"

    @staticmethod
    def clear():
        """wipe the terminal."""

        if OS_NAME == "posix":
            # *nix machines.
            system("clear")

        elif OS_NAME == "windows":
            system("cls")

        else:
            # for any os in the world.
            # system("your-command")
            pass

        return None
