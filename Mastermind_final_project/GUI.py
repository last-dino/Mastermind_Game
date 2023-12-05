import turtle
import time
from Point import Point
from Board import Board
from log_error import log_error


def create_canvas():
    """
    Function -- create_canvas
        creates and sets the size of the screen
    Parameters: None
    Returns: None
    """
    turtle.screensize(800, 1300)


def draw_frames():
    """
    Function -- draw_frames
        draws the frames for the guess board, control panel, and leaderboard
    Parameters: None
    Returns: None
    """
    guess_board = Board(Point(-400, 370), 450, 600)
    guess_board.draw_empty()

    control_panel = Board(Point(-400, -250), 800, 130)
    control_panel.draw_empty()

    leaderboard = Board(Point(100, 370), 300, 600, "green")
    leaderboard.draw_empty()


def create_leaderboard(filename):
    """
    Function -- create_leaderboard
        creates or displays the leaderboard from a file
    Parameters:
        filename (str) -- the name of the file containing leaderboard data
    Returns: None
    """
    try:
        display_file(filename)
    except FileNotFoundError as e:
        log_error(type(e).__name__)  # log error
        # pop up error gif
        display_gif("leaderboard_error.gif")
        with open(filename, "w") as out_file:
            out_file.write("Leaders:\n\n")
        display_file(filename)


def display_file(filename):
    """
    Function -- display_file
        displays the content of a file on the turtle graphics screen
    Parameters:
        filename (str) -- the name of the file to display
    Returns: None
    """
    with open(filename, "r") as in_file:
        turtle.penup()
        x, y = 150, 300
        line_spacing = 30
        turtle.goto(x, y)  # Set the position before writing
        turtle.color("blue")
        for line in in_file:
            turtle.write(line, align='left', font=('Arial', 16, 'bold'))
            y -= line_spacing
            turtle.goto(x, y)


def display_gif(gif_name):
    """
    Function -- display_gif
        displays a gif on the turtle graphics screen and clears it after a delay
    Parameters:
        gif_name (str) -- the name of the gif file
    Returns: None
    """
    turtle.up()
    turtle.goto(0, 0)
    turtle.down()
    turtle.addshape(gif_name)
    turtle.shape(gif_name)
    stamp_id = turtle.stamp()
    turtle.update()

    time.sleep(3)
    turtle.clearstamp(stamp_id)
