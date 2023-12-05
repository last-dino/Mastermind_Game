from Point import Point
from Marble import Marble


class BullsAndCows:
    """
    Class BullsAndCows
    Attributes: row, column, bulls_count, cows_count, total_bulls_and_cows
    Methods: fill_counts, create_total_bulls_and_cows
    """

    def __init__(self, row, column):
        """
        Constructor for the BullsAndCows class
        Parameters:
            row (int) -- the number of guesses allowed for a single game
            column (int): the number of colors for each guess
        """
        self.row = row
        self.column = column
        self.bulls_count = 0  # for convenient testing
        self.cows_count = 0  # for convenient testing
        self.total_bulls_and_cows = self.create_total_bulls_and_cows()

    def fill_counts(self, bulls, cows, index):
        """
        Method -- fill_counts
            fills the color for bulls and cows for the guess at the index
        Parameters:
            bulls (int) -- the count of bulls
            cows (int) -- the count of cows
            index (int) -- the index of the current guess
        """
        self.bulls_count = bulls
        self.cows_count = cows
        i = 0

        # fill in all bulls first, then all cows
        for _ in range(bulls):
            self.total_bulls_and_cows[index][i].set_color("black")
            self.total_bulls_and_cows[index][i].draw()
            i += 1
        for _ in range(cows):
            self.total_bulls_and_cows[index][i].set_color("red")
            self.total_bulls_and_cows[index][i].draw()
            i += 1

    def create_total_bulls_and_cows(self) -> list:
        """
        Method -- create_total_bulls_and_cows
            creates the display for all bulls and cows for a single game
        Returns a list representing all the bulls and cows display
        """
        x_1, x_2 = -40, -25  # x-coordinate for first and second column
        y_start = 323  # initial y-coordinate
        y_inner_spacing = 15  # vertical spacing for a single guess
        y_outer_spacing = 25  # vertical spacing between guesses
        total_bulls_and_cows = []
        y = y_start

        for _ in range(self.row):
            bulls_and_cows = []  # initialize a list for a single guess

            for i in range(self.column):
                if i % 2 == 0:  # two on the left column
                    marble = Marble(Point(x_1, y), size=4)

                else:  # two on the right column
                    marble = Marble(Point(x_2, y), size=4)
                    y -= y_inner_spacing  # adjust y-coordinate

                marble.draw_empty()
                bulls_and_cows.append(marble)

            total_bulls_and_cows.append(bulls_and_cows)
            y -= y_outer_spacing  # adjust y-coordinate

        return total_bulls_and_cows
