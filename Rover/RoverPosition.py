from Rover.RoverCoordinates import RoverCoordinates


class RoverPosition:

    coordinates: RoverCoordinates
    direction: str

    def __init__(self, coordinates, direction):
        self.coordinates = coordinates
        self.direction = direction
