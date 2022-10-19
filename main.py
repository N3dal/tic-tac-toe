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
from time import sleep
from random import randint, choice
from termcolor import colored
import json
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


class Map:
    """Represent the Game map"""

    def __init__(self, game_map: list = None, available_moves: list = None):

        pass
        # note if game map is none that mean start new game;
        # if its note none then load old game;

        if game_map is None or available_moves is None:
            # start new game;
            self.game_map = [
                ['1', '2', '3'],
                ['4', '5', '6'],
                ['7', '8', '9']
            ]

            self.available_moves = list("123456789")

        else:
            # load old game;
            self.game_map = game_map
            self.available_moves = available_moves

    def draw(self):
        """
        print the game map on the terminal screen;
        """
        # first clear;
        Tools.clear()

        print("""
╭───┬───┬───╮
│ {0} │ {1} │ {2} │
├───┼───┼───┤
│ {3} │ {4} │ {5} │
├───┼───┼───┤
│ {6} │ {7} │ {8} │
╰───┴───┴───╯
""".format(*sum(self.game_map, []))
        )

        return None

    def make_move(self, move: str, game_char: str):
        """update the game map values when the user or computer make moves;

        return None
        """
        # Tools.clear()

        for i, row in enumerate(self.game_map):
            for j, item in enumerate(row):

                if item == move:
                    self.game_map[i][j] = game_char

        # now update the terminal screen by re-draw the game-map;
        self.draw()

    def save(self):
        """
        save user and computer moves into file,
        and also save all available moves,
        so we can continue the game if we quit.

        return None;
        """

        with open(f"./{Tools.DEFAULT_FILE_NAME}", "w") as file:
            data_dictionary = {
                "game_map": self.game_map,
                "available_moves": self.available_moves
            }

            json.dump(data_dictionary, file)

        return None

    def who_win(self, user_char: str, computer_char: str):
        """
        checkout for any win moves on the game map.
        return "user" if the user win and return "computer" if computer win,
        and return "draw" if is draw, and if its return None that is mean the,
        game is still going;
        """
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

        for move in MOVES_TO_WIN:

            [i1, j1], [i2, j2], [i3, j3] = move

            temp_move = self.game_map[i1][j1] + \
                self.game_map[i2][j2] + self.game_map[i3][j3]

            if temp_move == (user_char*3):
                # if the user win;
                return "user"

            elif temp_move == (computer_char*3):
                # if the computer win;
                return "computer"

            else:
                # if its a draw;
                return "draw"

        # thats mean the game is still going;
        return None


class Dashboard:
    pass


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


def update_game_map(game_map: list, game_move: str, game_char: str):
    """update the game map with new moves and clear the terminal."""
    Tools.clear()

    for i, row in enumerate(game_map):
        for j, item in enumerate(row):

            if item == game_move:
                game_map[i][j] = game_char

    create_game_map(game_map)


def save_game_status_to_file(moves: list, available_moves: list):
    """save user and python moves into file,
    and also save all available moves,
    so we can continue the game if we quit."""

    DEFAULT_FILE_NAME = "last_game_data.json"

    with open(f"./{DEFAULT_FILE_NAME}", "w") as game_data_file:
        data_dictionary = {
            "game_map": moves,
            "available_moves": available_moves
        }

        json.dump(data_dictionary, game_data_file)


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


def win(game_map: list[list], python_char: str, usr_char: str):
    """checkout for any win moves on the game map.
    return 1 if the user win and return -1 if python win,
    and return 0 if is draw."""
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

    for move in MOVES_TO_WIN:

        [i1, j1], [i2, j2], [i3, j3] = move

        temp_move = game_map[i1][j1] + game_map[i2][j2] + game_map[i3][j3]

        if temp_move == (usr_char*3):
            return 1

        elif temp_move == (python_char*3):
            return -1


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

    game_map = [
        ['1', 'X', '3'],
        ['4', 'O', '6'],
        ['7', '8', 'O']
    ]

    available_moves = list("134678")

    start_game(game_map, available_moves)


if __name__ == "__main__":
    main_menu()
    main()
    dash_board({"Mike": 1, "python": 8})
