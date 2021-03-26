from InputController.InputReader import InputReader
from Plateau.Plateau import Plateau
from Rover.Rover import Rover

if __name__ == '__main__':
    #Read Inputs and check its syntax
    reader = InputReader()
    reader.readInputs("InputController/roverInputs.txt")

    #Initialize Plateau
    plateauDimensions = reader.getPlateauDimensions()
    Plateau.initializePlateau(plateauDimensions)

    print(f"Plateau dimensions {plateauDimensions.upper_right_x}, {plateauDimensions.upper_right_y}")
    print("------------------------------------------------------------------")

    #Iterate on the rovers and their instructions and start explorations in sequential order
    for p, i in reader.getRoversandInstructions():
        marsRover = Rover(p)
        Plateau.getInstance().addRover(marsRover)

        print(f"Input: {marsRover.position.coordinates.x} {marsRover.position.coordinates.y} {marsRover.position.direction}")

        marsRover.explorePlateau(i)
        print(f"Output: {marsRover.position.coordinates.x} {marsRover.position.coordinates.y} {marsRover.position.direction}")

        print("------------------------------------------------------------------\n")

    print(f"The plateau has {len(Plateau.getInstance().getRovers())} rovers that were able to navigate")

