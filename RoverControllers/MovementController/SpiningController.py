class SpiningController:
    """
        Allows the rover to spin 90 degrees left or right, without moving from its current spot.
    """

    directions = ["N", "E", "S", "W"]

    def __spinLeft(self, direction):
        return self.directions[self.directions.index(direction) - 1]

    def __spinRight(self, direction):
        return self.directions[(self.directions.index(direction) + 1) % len(self.directions)]

    def spin(self, instruction, direction):
        if instruction == "R":
            return self.__spinRight(direction)
        elif instruction == "L":
            return self.__spinLeft(direction)

