import Plateau.Plateau as plt
from Exceptions.MovementException import RoverOutsidePlateauException, NextSpotNotEmptyException
from Rover.RoverCoordinates import RoverCoordinates


class MovementValidator:
    @staticmethod
    def canMove(rover_coordinates: RoverCoordinates, move_x: int, move_y: int):
        newCoordinates = RoverCoordinates(rover_coordinates.x + move_x, rover_coordinates.y + move_y)

        return (MovementValidator.isEmptySpot(newCoordinates)) and (
            MovementValidator.isRoverInsidePlateau(newCoordinates))

    @staticmethod
    def isEmptySpot(rover_coordinates: RoverCoordinates):
        plateau_rovers = plt.Plateau.getInstance().getRovers()
        for r in plateau_rovers:
            if r.position.coordinates == rover_coordinates:
                raise NextSpotNotEmptyException(rover_coordinates)
        return True

    @staticmethod
    def isRoverInsidePlateau(rover_coordinates: RoverCoordinates):
        plateau_dimensions = plt.Plateau.getInstance().getDimensions()
        if not ((0 <= rover_coordinates.x <= plateau_dimensions.upper_right_x) and (
                0 <= rover_coordinates.y <= plateau_dimensions.upper_right_y)):
            raise RoverOutsidePlateauException(rover_coordinates)
        return True
