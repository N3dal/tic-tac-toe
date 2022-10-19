from random import randint, choice


class Computer:
    """"""

    def __init__(self, computer_char: str):
        self.__computer_char = computer_char

    @property
    def char(self):
        """the char that the computer use to play;"""
        return self.__computer_char

    def get_move(self, available_moves: list[str]):
        """generate random move from the available ones,
        for python."""

        return choice(available_moves)


class User:
    """"""

    def __init__(self, user_char: str):

        self.__user_char = user_char

    @property
    def char(self):
        """the char that the user use to play;"""
        return self.__user_char

    @staticmethod
    def get_input(msg: str):
        return input(msg).strip().lower()

    def get_move(self, available_moves):
        """
        ask the user about the next move,
        and make sure that move in the right range,
        and its available.

        return str;
        """

        usr_move = self.get_input("Choose one move from the available ones: ")

        while usr_move not in available_moves:
            print("this move isn't available!!")
            usr_move = get_usr_input(
                "Choose one move from the available ones: ")

        return usr_move


u = User("x")
c = Computer('o')
