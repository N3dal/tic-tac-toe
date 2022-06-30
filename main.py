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
from random import randint, choice


# link for lines that i used for drawing the game map:
# https: // en.wikipedia.org/wiki/Box-drawing_character

# TODO: add resume future, so save the player progress in json file.
# TODO: and when its play again ask them to continue or not.
# TODO: add line when you win cut the x line or o line.

# possible moves for user or python to win.
MOVES_TO_WIN = [
    # horizontal moves to win.
    ([0, 0], [0, 1], [0, 2]),
    ([1, 0], [1, 1], [1, 2]),
    ([2, 0], [2, 1], [2, 2]),

    # vertical moves to win.
    ([0, 0], [1, 0], [2, 0]),
    ([0, 1], [1, 1], [2, 1]),
    ([0, 2], [1, 2], [2, 2]),

    # diagonal moves to win.
    ([0, 0], [1, 1], [2, 2]),
    ([0, 2], [1, 1], [2, 0])

]


def clear():
    """wipe the terminal."""

    if OS_NAME == "posix":
        # *nix machines.
        system("clear")

    else:
        # windows machines.
        system("cls")


clear()


def create_game_map(game_map):
    """draw the game map"""

    game_map = """
╭───┬───┬───╮
│ {0} │ {1} │ {2} │
├───┼───┼───┤
│ {3} │ {4} │ {5} │
├───┼───┼───┤
│ {6} │ {7} │ {8} │
╰───┴───┴───╯
""".format(*sum(game_map, []))
    print(game_map)


def get_usr_input(msg: str):
    """"""

    return input(msg).strip().lower()


def set_characters():
    """ask the users about the character they want,
    to play with it and get it from them, and select,
    character for python too depending on the user character.

    simply-out get the users character by asking them.
    return tuple contain two strings,
    values one for user-char and the another,
    one for python-char."""
    usr_char = get_usr_input("Choose 'X' or 'O': ")
    while usr_char not in ('x', 'o'):
        # keep asking the user.
        usr_char = get_usr_input("Choose 'X' or 'O': ")

    return usr_char, ('x' if usr_char == 'o' else 'o')


def get_usr_move(available_moves: list[str]):
    """ask the user about the next move,
    and make sure that move in the right range,
    and its available."""

    usr_move = get_usr_input("Choose one move from the available ones: ")

    while usr_move not in available_moves:
        print("this move isn't available!!")
        usr_move = get_usr_input("Choose one move from the available ones: ")

    return usr_move


def get_python_move(available_moves: list[str]):
    """generate random move from the available ones,
    for python."""

    return choice(available_moves)


def update_game_map(game_map: list, usr_move: str, usr_char: str):
    """update the game map with new moves and clear the terminal."""
    clear()

    for i, row in enumerate(game_map):
        for j, item in enumerate(row):

            if item == usr_move:
                game_map[i][j] = usr_char

    create_game_map(game_map)


def main():
    game_map = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]

    available_moves = list("123456789")

    # ask the users which char they want to play with,
    # and keep asking them until they give the right character.
    usr_char, python_char = set_characters()

    create_game_map(game_map)

    while available_moves:

        usr_move = get_usr_move(available_moves)
        python_move = get_python_move(available_moves)

        available_moves.pop(available_moves.index(usr_move))
        available_moves.pop(available_moves.index(python_move))

        update_game_map(game_map, usr_move, usr_char)
        update_game_map(game_map, python_move, python_char)


if __name__ == "__main__":
    main()
