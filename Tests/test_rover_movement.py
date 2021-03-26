import pytest
from Exceptions.MovementException import RoverOutsidePlateauException, NextSpotNotEmptyException
from InputController.InputReader import InputReader
from Exceptions.InputsException import *

from Plateau.Plateau import Plateau
from Plateau.PlateauDimensions import PlateauDimensions
from Rover.Rover import Rover
from Rover.RoverCoordinates import RoverCoordinates
from Rover.RoverPosition import RoverPosition


@pytest.fixture
def get_plateau():
    return Plateau.initializePlateau(PlateauDimensions(5, 5))


@pytest.mark.parametrize("x, y, direction, instructions,expected_x, expected_y, expected_direction", [
    (1, 3, "N", "L", 1, 3, "W"),
    (0, 2, "E", "RRR", 0, 2, "N"),
    (1, 0, "E", "LLL", 1, 0, "S"),
    (3, 0, "W", "LRRLLLRL", 3, 0, "E")
])
def testExploringWithSpining(x, y, direction, expected_x, instructions, expected_y, expected_direction):
    rover = Rover(RoverPosition(RoverCoordinates(x, y), direction))
    rover.explorePlateau(instructions)
    assert (rover.position.coordinates.x == expected_x) and (rover.position.coordinates.y == expected_y) and (
            rover.position.direction == expected_direction)


@pytest.mark.parametrize("x, y, direction, instructions ,expected_x, expected_y, expected_direction", [
    (1, 3, "N", "M", 1, 4, "N"),
    (0, 2, "E", "MMM", 3, 2, "E"),
])
def testExploringWithMoving(get_plateau, x, y, direction, expected_x, instructions, expected_y, expected_direction):
    rover = Rover(RoverPosition(RoverCoordinates(x, y), direction))
    rover.explorePlateau(instructions)
    assert (rover.position.coordinates.x == expected_x) and (rover.position.coordinates.y == expected_y) and (
            rover.position.direction == expected_direction)


@pytest.mark.parametrize("x, y, direction, instructions ,expected_x, expected_y, expected_direction", [
    (1, 2, "N", "LMLMLMLMM", 1, 3, "N"),
    (3, 3, "E", "MMRMMRMRRM", 5, 1, "E")
])
def testExploringMovingAndSpining(get_plateau, x, y, direction, expected_x, instructions, expected_y,
                                  expected_direction):
    rover = Rover(RoverPosition(RoverCoordinates(x, y), direction))
    rover.explorePlateau(instructions)
    assert (rover.position.coordinates.x == expected_x) and (rover.position.coordinates.y == expected_y) and (
            rover.position.direction == expected_direction)


@pytest.mark.parametrize("x, y, direction, instructions ,expected_x, expected_y, expected_direction", [
    (0, 0, "S", "M", 0, 0, "S"),
    (5, 5, "N", "M", 5, 5, "N"),
])
def testMoveOutsidePlateau(get_plateau, x, y, direction, expected_x, instructions, expected_y, expected_direction):
    with pytest.raises(RoverOutsidePlateauException):
        rover = Rover(RoverPosition(RoverCoordinates(x, y), direction))
        rover.explorePlateau(instructions)


@pytest.mark.parametrize("x, y, direction, instructions", [
    (1, 0, "N", "M")
])
def testRoversCollision(get_plateau, x, y, direction, instructions):
    Plateau.getInstance().addRover(Rover(RoverPosition(RoverCoordinates(1, 1), "N")))
    with pytest.raises(NextSpotNotEmptyException):
        rover = Rover(RoverPosition(RoverCoordinates(x, y), direction))
        rover.explorePlateau(instructions)

