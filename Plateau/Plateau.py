from Plateau.PlateauDimensions import PlateauDimensions
from Rover.Rover import Rover


class Plateau:
    """
    The plateau is a singleton, described by its dimensions and rovers moving on its grid.
    """
    __dimensions: PlateauDimensions
    __rovers: list
    __instance = None

    @staticmethod
    def initializePlateau(dimensions: PlateauDimensions):
        if Plateau.__instance == None:
            Plateau()
            Plateau.__instance.__dimensions = dimensions
        return Plateau.__instance

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Plateau.__instance == None:
            raise Exception("The plateau should be initialized at first!")
        return Plateau.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Plateau.__instance != None:
            raise Exception("Can't instantiate a plateau. It should be initialized! please call initializePlateau")
        else:
            Plateau.__instance = self
            self.__rovers = []

    def getDimensions(self):
        return self.__dimensions

    def getRovers(self):
        return self.__rovers

    def addRover(self, rover: Rover):
        self.__rovers.append(rover)
