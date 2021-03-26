import re
from Exceptions.InputsException import *
from Plateau.PlateauDimensions import PlateauDimensions
from Rover.RoverCoordinates import RoverCoordinates
from Rover.RoverPosition import RoverPosition


class InputReader:
    """
    Reads the user input and checks its syntax.
    """
    input: str

    def readInputs(self, filepath):
        """
        Read inputs file
        :param A Text file contains at least 3 lines. first line represents plateau dimensions, the second indicates rover's
        position and the third contains the movement instructions.
        """
        with open(filepath) as reader:
            self.input = reader.readlines()
            self.__checkInput()

    def __checkInput(self):
        """
        Checks the input structure:
        - The file should contains at least 3 lines.
        - Each rover has its own instructions i.e: number of rows of file - 1 must be pair.
        """
        if len(self.input) < 3:
            raise FileInputsContentException
        if (len(self.input) - 1) % 2 != 0:
            raise FileInputFormatException

    def __getRoverPosition(self, roverPosition: str):
        """
        Get the rover position if its syntax respects Input Regex for rover Position : x y D
        :param a string of rover position
        :return: a RoverPosition
        """
        matched = re.match("(?P<x>[0-9]+?) *(?P<y>[0-9]+?) *(?P<D>[NESW]{1}?) *$", roverPosition)
        if not bool(matched):
            raise RoverPositionInputException(roverPosition)

        result = matched.groupdict()
        return RoverPosition(RoverCoordinates(int(result["x"]), int(result["y"])), result["D"])


    def __getRoverInstruction(self, instructions: str):

        """
        Get the movement instructions if its syntax respects Input Regex for rover Instruction : MLR

        :param: input instructions
        :return: instructions
        """
        matched = re.match("(?P<instructions>[MLR]+?) *$", instructions)

        if not bool(matched):
            raise MovementInstructionsInputException

        return matched.groupdict()["instructions"]

    def getPlateauDimensions(self):
        """
        :return: Plateau dimensions : upper_right_x, upper_right_y
        """
        # Check if respects Input Regex for coordinates : X Y
        matched = re.match("(?P<X>[0-9]+?) *(?P<Y>[0-9]+?) *$", self.input[0])
        if not bool(matched):
            raise PlateauDimensionsInputException
        result = matched.groupdict()
        return PlateauDimensions(int(result["X"]), int(result["Y"]))

    def getRoversandInstructions(self):
        """
        extract (rover, instruction) iteratively
        :return: iterator
        """
        for i in range(1, len(self.input), 2):
            roverPosition = self.__getRoverPosition(self.input[i])
            roverInstructions = self.__getRoverInstruction(self.input[i + 1])

            yield (roverPosition, roverInstructions)
