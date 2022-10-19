"""
    all the tools and the defaults needed for the game to work;

"""


class Tools:
    """"""

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
