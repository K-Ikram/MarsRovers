"""
This file contains custom exceptions about rover movement
"""
class RoverOutsidePlateauException(Exception) :
    def __init__(self, coordinates):
        self.message = f"Cannot go outsite the plateau, current position {coordinates.x} {coordinates.y}"
        super().__init__(self.message)

class NextSpotNotEmptyException(Exception) :
    def __init__(self, coordinates):
        self.message = f"Cannot move to next spot {coordinates.x} {coordinates.y} because it's not empty!"
        super().__init__(self.message)
