import turtle
from Point import Point

SIZE = 30


class Button:
    """
    Class Button
    Attributes: position, image_name, size
    Methods: new_pen, get_color, draw, clicked_in_region
    """
    def __init__(self, position, image_name, size=SIZE):
        """
        Constructor for the Button class
        Parameters:
            position (Point) -- the position of the button
            image_name (str) -- the name of the image file for the button
            size (int) -- the radius of the button
        """
        self.pen = self.new_pen()
        self.name = image_name
        self.position = position
        self.size = size
        self.pen.speed(0)  # set to the fastest drawing

    def new_pen(self):
        """
        Method -- new_pen
            creates a new turtle pen
        Returns a new turtle pen
        """
        return turtle.Turtle()

    def get_color(self):
        """
        Method -- get_color
            extracts the name of the button from the filename
            use get_color protocol to align with the color buttons
        Returns a string of the name of the button
        """
        color = self.name.split(".")
        return color[0]

    def draw(self):
        """
        Method -- draw
            Draws the button on the screen
        Returns None
        """
        self.pen.up()
        self.pen.setpos(self.position.x, self.position.y)
        turtle.addshape(self.name)  # register the image
        self.pen.shape(self.name)
        self.pen.down()

    def clicked_in_region(self, x, y):
        """
        Method -- clicked_in_region
            checks if a click is within the button region
        Parameters:
            x (float) -- the x-coordinate of the click
            y (float) -- the y-coordinate of the click
        Returns a bool (True if the click is within the button region,
            False otherwise)
        """
        if abs(x - self.position.x) <= self.size and \
                abs(y - self.position.y) <= self.size:
            return True
        return False
