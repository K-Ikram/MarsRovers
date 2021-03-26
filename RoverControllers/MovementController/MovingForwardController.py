from Rover.RoverCoordinates import RoverCoordinates
from Validators.MovementValidator import MovementValidator


class MovingForwardController:
    """
    Allows the rover to move forward one grid point, and maintain the same heading.
    """
    dict_position = {
        "N": (0, 1),
        "E": (1, 0),
        "S": (0, -1),
        "W": (-1, 0),
    }

    def moveAStep(self, coordinates: RoverCoordinates, direction: str):
        move_x, move_y = self.dict_position[direction]
        if MovementValidator.canMove(coordinates, move_x, move_y):
            coordinates.x += move_x
            coordinates.y += move_y
        return coordinates
