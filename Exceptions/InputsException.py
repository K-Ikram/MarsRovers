"""
This file contains custom exceptions for input errors.
"""

class FileInputFormatException(Exception):
    def __init__(self):
        self.message = "File format invalid ! please refer to manual"
        super().__init__(self.message)

class FileInputsContentException(Exception):
    def __init__(self):
        self.message = "File does not contain all inputs (at least 3 lines)!"
        super().__init__(self.message)

class RoverPositionInputException(Exception):
    def __init__(self, roverPosition):
        self.message = f"Input invalid: rover position {roverPosition} is invalid! use x y D where (x,y) are integers and D is (L or R)"
        super().__init__(self.message)

class MovementInstructionsInputException(Exception):
    def __init__(self):
        self.message = "Input invalid: rover instructions must be one of the following M, L, R"
        super().__init__(self.message)

class PlateauDimensionsInputException(Exception):
    def __init__(self):
        self.message ="Input invalid: The first line of input is the upper-right coordinates of the plateau"
        super().__init__(self.message)
