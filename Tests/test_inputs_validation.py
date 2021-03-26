import pytest

from Exceptions.InputsException import RoverPositionInputException
from InputController.InputReader import InputReader


def testValidateDirectionNameInput():
    with pytest.raises(RoverPositionInputException):
        reader = InputReader()
        reader.readInputs("TestFiles/testDirectionNameInput")
        next(reader.getRoversandInstructions())