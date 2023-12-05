import turtle
from Point import Point


class Shape:
    """
    Class Shape
    Attributes: position, color, is_empty
    Methods: new_pen, set_color, get_color, get_empty_state, draw_empty, erase
    """
    def __init__(self, position, color):
        """
        Constructor for the Shape class
        Parameters:
            position (Point) -- the position of the shape
            color (str) -- the color of the shape
        """
        self.pen = self.new_pen()
        self.color = color
        self.position = position
        self.is_empty = True
        self.pen.hideturtle()
        self.pen.speed(0)  # set to the fastest drawing

    def new_pen(self):
        """
        Method -- new_pen
            creates a new turtle pen
        Returns a new turtle pen
        """
        return turtle.Turtle()

    def set_color(self, color):
        """
        Method -- set_color
            sets the color of the shape
        Parameters:
            color (str) -- the color to set
        """
        self.color = color
        self.is_empty = False

    def get_color(self):
        """
        Method -- get_color
            gets the color of the shape
        Returns a str of the color of the shape
        """
        return self.color

    def draw_empty(self):
        """
        Method -- draw_empty
            draws an empty shape on the screen
        """
        self.erase()
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.is_empty = True
        self.pen.down()

    def erase(self):
        """
        Method -- erase
            clear the shape on the screen
        """
        self.pen.clear()
