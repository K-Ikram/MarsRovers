from RoverControllers.IRoverController import IRoverController
from RoverControllers.MovementController.MovingForwardController import MovingForwardController
from RoverControllers.MovementController.SpiningController import SpiningController
from Rover.RoverPosition import RoverPosition


class RoverMovementController(IRoverController):
    """
        Controls the rover movement. it dispatches the instruction to corresponding movement controller (spinning or
         moving forward one step)
    """
    __spiningController: SpiningController
    __movingController: MovingForwardController

    def __init__(self):
        self.__spiningController = SpiningController()
        self.__movingController = MovingForwardController()

    def start_action(self, instructions: str, position: RoverPosition):

        for instruction in instructions:
            if instruction == "M":
                position.coordinates = self.__movingController.moveAStep(position.coordinates, position.direction)
            else:
                position.direction = self.__spiningController.spin(instruction, position.direction)

        return position
