from RoverControllers.IRoverController import IRoverController
from RoverControllers.MovementController.RoverMovementController import RoverMovementController
from Rover.RoverPosition import RoverPosition


class Rover:
    """
    Rover is described by its positions (coordinates and direction).
    it can explore the Plateau by moving forward on its grid or by spinning 90 degrees left or right. the movement controller
    manages this movement.
    """
    position: RoverPosition
    movementController: IRoverController

    def __init__(self, position: RoverPosition):
        self.position = position

    def explorePlateau(self, instructions):
        movementCtrl = RoverMovementController()
        self.position = movementCtrl.start_action(instructions, self.position)

