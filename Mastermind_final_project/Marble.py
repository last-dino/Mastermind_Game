from Shape import Shape

MARBLE_RADIUS = 20


class Marble(Shape):
    """
    Class Marble(Subclass of Shape)
    Attributes: position, color, size
    Methods: draw, draw_empty, get_empty_state, clicked_in_region
    """

    def __init__(self, position, color="black", size=MARBLE_RADIUS):
        """
        Constructor for the Marble class
        Parameters:
            position (Point) -- the position of the center of the circle
            color (str, optional) -- the color to fill the circle
            size (int) -- the radius of the circle
        """
        # call parent constructor with position and color
        super().__init__(position, color)
        self.size = size

    def draw(self):
        """
        Method -- draw
            draws a filled circle with the chosen color
        """
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.is_empty = False
        self.pen.down()
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        self.pen.circle(self.size)
        self.pen.end_fill()

    def draw_empty(self):
        """
        Method -- draw_empty
            draws an empty circle
        """
        super().draw_empty()
        self.pen.circle(self.size)

    def get_empty_state(self):
        """
        Method -- get_empty_state
            gets the empty state of the shape
        Returns a bool, true if the shape is empty, False otherwise
        """
        return self.is_empty

    def clicked_in_region(self, x, y):
        """
        Method -- clicked_in_region
            checks if a click is within the circle region
        Parameters:
            x (float) -- the x-coordinate of the click
            y (float) -- the y-coordinate of the click
        Returns a bool (True if the click is within the circle region,
            False otherwise)
        """
        if abs(x - self.position.x) <= self.size and \
                abs(y - self.position.y) <= self.size:
            return True
        return False
