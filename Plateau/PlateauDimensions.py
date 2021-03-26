class PlateauDimensions:

    """
    Custom Plateau dimensions type.
    """
    upper_right_x: int
    upper_right_y: int

    def __init__(self, upper_right_x, upper_right_y):
        self.upper_right_x = upper_right_x
        self.upper_right_y = upper_right_y