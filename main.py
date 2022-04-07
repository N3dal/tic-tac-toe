#!/usr/bin/python3
# -----------------------------------------------------------------
# simple tic tac toe game.
#
#
#
# Author:N84.
#
# Create Date:Thu Apr  7 15:27:45 2022.
# ///
# ///
# ///
# -----------------------------------------------------------------

from os import name as OS_NAME
from os import system
from time import sleep
from random import randint


# link for lines that i used for drawing the game map:
# https: // en.wikipedia.org/wiki/Box-drawing_character

def clear():
    """wipe the terminal."""

    if OS_NAME == "posix":
        # *nix machines.
        system("clear")

    else:
        # windows machines.
        system("cls")


def main():
    pass


if __name__ == "__main__":
    main()
