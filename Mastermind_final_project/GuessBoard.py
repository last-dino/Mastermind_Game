from Point import Point
from Marble import Marble
from Arrow import Arrow


X_SPACING, Y_SPACING = 60, 55
X_START, Y_START = -290, 300

class GuessBoard:
    """
    Class GuessBoard
    Attributes: row, column, guesses, count_within_row, won, quit, total_guesses
    Methods: get_guesses, get_won_status, set_won_status_to_true, get_quit_status, set_quit_status_to_true,
        get_count_within_row, on_green_check_button_click, on_red_cross_button_click, on_color_click,
        create_total_guesses
    """
    def __init__(self, row, column):
        """
        Constructor for the GuessBoard class.
        Parameters:
            row (int) -- the number of guesses
            column (int) -- the number of colors in each guess
        """
        self.row = row
        self.column = column
        self.guesses = 0  # record current guess
        self.count_within_row = 0  # record current color within a guess

        # create and draw the arrow
        self.arrow = Arrow(Point(X_START - 70, Y_START + 40))
        self.arrow.draw()
        self.won = False
        self.quit = False
        self.total_guesses = self.create_total_guesses()

    def get_guesses(self):
        """
        Method -- get_guesses
        Returns an int that is the index of the current guess,
            which also represents the amount of guesses made so far
        """
        return self.guesses

    def get_count_within_row(self):
        """
        Method -- get_count_within_row
        Returns an int that represents the index of the color
            within the current guess
        """
        return self.count_within_row

    def get_won_status(self):
        """
        Method -- get_won_status
        Returns a bool represents the current winning state
        """
        return self.won

    def set_won_status_to_true(self):
        """
        Method -- set_won_status_to_true
            sets the current winning state to true
        """
        self.won = True

    def get_quit_status(self):
        """
        Method -- get_quit_status
        Returns a bool represents the current status for quitting
        """
        return self.quit

    def set_quit_status_to_true(self):
        """
        Method -- set_quit_status_to_true
            sets the current status for quitting to true
        """
        self.quit = True

    def on_green_check_button_click(self):
        """
        Method -- on_green_check_button_click
        Returns a list of the current guess made by player
        """
        # the row must be full to get here, return the row
        current_row = []
        for each in self.total_guesses[self.guesses]:
            current_row.append(each.get_color())

        self.guesses += 1  # set to next guess
        self.count_within_row = 0  # set to the first color

        self.arrow.erase()  # update the arrow location
        if self.guesses < 10:  # redraw arrow if there's guess left
            self.arrow.set_y(self.arrow.get_y() - Y_SPACING)
            self.arrow.draw()

        return current_row

    def on_red_cross_button_click(self):
        """
        Method -- on_red_cross_button_click
            restart the current guess
        """
        # empty the row
        for each in self.total_guesses[self.guesses]:
            each.draw_empty()

        self.count_within_row = 0  # reset to the first color

    def on_color_click(self, color: str) -> bool:
        """
        Method -- on_color_click
            add a color to the guess if there's at least one slot left
        Returns a bool to indicate if the color is
            added to the guess successfully
        """
        success = False  # initialize flag to false

        # only proceed if there's color left to guess
        if self.guesses < self.row and self.count_within_row < self.column:
            self.total_guesses[self.guesses][self.count_within_row].set_color(color)
            self.total_guesses[self.guesses][self.count_within_row].draw()
            self.count_within_row += 1
            success = True

        return success

    def create_total_guesses(self) -> list:
        """
        Method -- create_total_guesses
            creates the display for all guesses for a single game
        Returns a list representing all the guesses display
        """
        total_guesses = []
        x, y = X_START, Y_START

        for _ in range(self.row):
            guess = []  # initialize a list for a single guess

            for _ in range(self.column):
                marble = Marble(Point(x, y))
                marble.draw_empty()
                guess.append(marble)
                x += X_SPACING  # adjust x-coordinate

            total_guesses.append(guess)
            x = X_START  # reset x-coordinate to the first column
            y -= Y_SPACING  # adjust y-coordinate

        return total_guesses
