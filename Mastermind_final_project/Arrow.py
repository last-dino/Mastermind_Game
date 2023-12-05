from Shape import Shape


class Arrow(Shape):
    """
    Class Arrow(Subclass of Shape)
    Attributes: position, color
    Methods: get_y, set_y, draw, draw_arrow
    """

    def __init__(self, position, color="red"):
        """
        Constructor for the Arrow class
        Parameters:
            position (Point) -- the position of the top-left corner of the board
            color (str, optional) -- the color of the board, default to "red"
        """
        # call parent constructor with position and color
        super().__init__(position, color)

    def get_y(self):
        """
        Method -- get_y
            get the y-coordinate of the arrow
        """
        return self.position.y

    def set_y(self, y):
        """
        Method -- set_y
            change the y-coordinate of the arrow
        Parameters:
            y (Float) -- the new y-coordinate
        """
        self.position.y = y

    def draw(self):
        """
        Method -- draw
            draws a filled arrow at its position
        """
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.is_empty = False
        self.pen.down()
        self.pen.width(3)
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        self.draw_arrow()
        self.pen.end_fill()

    def draw_arrow(self):
        """
        Method -- draw_arrow
            draws an arrow
        """
        self.pen.setheading(-30)
        self.pen.forward(40)

        self.pen.right(120)
        self.pen.forward(40)

        self.pen.right(150)
        self.pen.forward(23)

        self.pen.left(60)
        self.pen.forward(23)

