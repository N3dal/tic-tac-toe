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

from tools import Tools
from game_map import Map
from players import (User, Computer)
from time import sleep
from random import randint, choice
from termcolor import colored
from sys import exit as _exit


# link for lines that i used for drawing the game map:
# https: // en.wikipedia.org/wiki/Box-drawing_character

# TODO: add continue future, so save the player progress and scores in json file.
# TODO: and when its play again ask them to continue or not.
# TODO: add line when user win cuts the x line or o line.
# TODO: add dash-board for points.
# TODO: add Colors to your terminal => Done.
# TODO: add username to file and save all the scores, for ex: how many time,
# TODO: this user win or lose and average, and add timer to see how it take for each round.
# TODO: add settings options to the game.

# wipe terminal screen;
Tools.clear()


class Dashboard:
    pass


def set_characters():
    """ask the users about the character they want,
    to play with it and get it from them, and select,
    character for python too depending on the user character.

    simply-out get the users character by asking them.
    return tuple contain two strings,
    values one for user-char and the another,
    one for python-char."""
    usr_char = get_usr_input(
        f"Choose{colored(''' 'X' ''', 'red')}or{colored(''' 'O' ''', 'blue')}': ")
    while usr_char not in ('x', 'o'):
        # keep asking the user.
        usr_char = get_usr_input("Choose 'X' or 'O': ")

    # note: colored function return a "str" object.
    if usr_char.upper() == "X":
        # the user char here is 'X'.
        return colored("X", "red"), colored("O", "blue")

    else:
        # the user char here is 'O'.
        return colored("O", "blue"), colored("X", "red")


def dash_board(game_score_data: dict):
    """create the dashboard and show to the users.
    this dashboard contain the username and all,
    scores for that user."""

    (username, user_score), (python, python_score) = game_score_data.items()

    # first convert scores from integer to str,
    # and make sure to fill with zeros.
    user_score = str(user_score).zfill(2)
    python_score = str(python_score).zfill(2)

    # add colors to username and the scores.
    username = colored(username, "red")
    python = colored(python, "green")

    user_score = colored(user_score, "yellow")
    python_score = colored(python_score, "yellow")

    top_line = "╭───────────────────┬──────────────────╮"
    mid_line = "│    {0}   │     {1}      │".format
    sep_line = "├───────────────────┼──────────────────┤"
    bottom_line = "╰───────────────────┴──────────────────╯"

    # print out the dashboard.
    print(top_line)
    print(mid_line(username.center(21), python.center(16)))
    print(sep_line)
    # note: colored work as str functor so it will,
    # convert an integer type to str, so we can use,
    # center method.
    print(mid_line(user_score.center(21), python_score.center(16)))
    print(bottom_line)


def main_menu():
    """draw the game main menu for the users."""

    # first clear terminal screen.
    Tools.clear()

    # create tuple that contain game_option names and their colors.
    GAME_OPTIONS = (
        ("New Game", "green"),
        ("Load Game", "yellow"),
        ("Settings", "blue"),
        ("Exit", "red")
    )

    for index, (option_name, color) in enumerate(GAME_OPTIONS, 1):

        menu_option = colored(f"[{index}] {option_name}", color).center(80)

        print(menu_option)

    usr_option = get_usr_input(": ")

    if usr_option not in [*"1234"]:
        # if the user give us wrong input,
        # or option out of range.
        main_menu()

    if usr_option == "1":
        # start New-game.
        _new_game()

    elif usr_option == "2":
        # load Old-game from game data file.
        pass

    elif usr_option == "3":
        # open the setting page.
        pass

    else:
        # kill the program and quit.
        _exit()


def _new_game():
    """"""
    Tools.clear()
    start_game()


def start_game(game_map: list = None, available_moves: list = None):
    """start either new game or load old game depending on,
    the function args if we pass game_map list and available_moves,
    list to this function that's mean we will load an old game,
    and if we not pass any arg then we will start new game."""

    if game_map is None:
        game_map = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]

    if available_moves is None:
        available_moves = list("123456789")

    # ask the user about the name.

    usr_name = get_usr_input(colored("Give your username: ", "yellow"))

    # ask the users which char they want to play with,
    # and keep asking them until they give the right character.
    usr_char, python_char = set_characters()

    create_game_map(game_map)

    while available_moves:

        usr_move = get_usr_move(available_moves)
        # now remove the move from the available moves.
        available_moves.pop(available_moves.index(usr_move))
        update_game_map(game_map, usr_move, usr_char)

        if available_moves:
            # make sure that the moves not empty when,
            # generating a random move.
            python_move = get_python_move(available_moves)

            # now remove the move from the available moves.
            # and make sure the moves list is not empty.
            available_moves.pop(available_moves.index(python_move))
        update_game_map(game_map, python_move, python_char)

        save_game_status_to_file(game_map, available_moves)

        if win(game_map, python_char, usr_char) == 1:
            # when the user win.
            print(colored(f"Good Job '{usr_name}' you win.", "green"))
            break
        elif win(game_map, python_char, usr_char) == -1:
            # when python aka computer win.
            print(
                colored(f"Ohh no '{usr_name}', python win and you lose.", "red"))
            break
    else:
        # if we got a draw.
        print(colored(f"Draw....", "yellow"))


def main():

    game_map = Map()

    # set the user and the computer chars;
    user_char, computer_char = set_characters()

    user = User(user_char)
    computer = Computer(computer_char)

    game_map.draw()

    while game_map.available_moves:

        usr_move = user.get_move(game_map.available_moves)
        game_map.make_move(usr_move, user.char)

        cmp_move = computer.get_move(game_map.available_moves)
        game_map.make_move(cmp_move, computer_char)

        game_map.save()

        result = game_map.who_win(user.char, computer.char)

        if result == "user":
            print("user win")

        elif result == "computer":
            print("computer win")

        elif result == "draw":
            print("draw")


if __name__ == "__main__":
    # main_menu()
    main()
    # dash_board({"Mike": 1, "python": 8})
