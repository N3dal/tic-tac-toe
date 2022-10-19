

from tools import Tools
import json


class Map:
    """Represent the Game map"""

    def __init__(self, game_map: list = None, available_moves: list = None):

        pass
        # note if game map is none that mean start new game;
        # if its not none then load old game;

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

                    # now remove the move from the available moves;
                    self.available_moves.remove(move)

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
            # print(len(self.available_moves))

            if temp_move == (user_char*3):
                # if the user win;
                return "user"

            elif temp_move == (computer_char*3):
                # if the computer win;
                return "computer"

            if len(self.available_moves) == 0:
                # if its a draw;
                return "draw"

        # thats mean the game is still going;
        return None


m = Map()

m.make_move("3", "x")
m.make_move("2", "x")
m.make_move("5", "x")
# m.make_move("4", "x")
# m.make_move("9", "x")


m.make_move("6", "o")
# m.make_move("7", "o")
# m.make_move("8", "o")
# m.make_move("1", "o")

print(m.who_win("x", "o"))
m.save()
