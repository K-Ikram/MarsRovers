class RoverCoordinates:
    """
    Custom type of rover coordinates.
    """
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, obj):
        return  isinstance(obj, RoverCoordinates) and (obj.x == self.x) and (obj.y == self.y)