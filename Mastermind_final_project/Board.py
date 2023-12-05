from Shape import Shape


class Board(Shape):
    """
    Class Board(Subclass of Shape)
    Attributes: position, width, height, color
    Methods: draw_empty, draw_rectangle
    """

    def __init__(self, position, width, height, color="black"):
        """
        Constructor for the Board class
        Parameters:
            position (Point) -- the position of the top-left corner of the board
            width (int) -- the width of the board
            height (int) -- the height of the board
            color (str, optional) -- the color of the board, default to "black"
        """
        # call parent constructor with position and color
        super().__init__(position, color)
        self.width = width
        self.height = height

    def draw_empty(self):
        """
        Method -- draw_empty
            draws a hollow board(rectangle) in the color chosen
        """
        super().draw_empty()  # inherits from parent
        self.pen.width(8)  # set line thickness
        self.pen.color(self.color)
        self.draw_rectangle(self.width, self.height)

    def draw_rectangle(self, width, height):
        """
        Method -- draw_rectangle
            draws a rectangle
        Parameters:
            width (int) -- the width of the rectangle
            height (int) -- the height of the rectangle
        """
        self.pen.setheading(270)
        self.pen.forward(height)
        self.pen.left(90)

        self.pen.forward(width)
        self.pen.left(90)

        self.pen.forward(height)
        self.pen.left(90)

        self.pen.forward(width)
        self.pen.left(90)