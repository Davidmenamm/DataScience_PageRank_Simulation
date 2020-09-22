# Class to coordinate page rank and random walker algorithm

# imports
from PowerIteration import PowerIteration


class Coordinator:
    # constructor
    def __init__(self, matrix):
        # atributes
        self.matrix = matrix  # current matrix, changes when teleported

    # to run power iteration algorithm
    def runPowerIteration(self):
        # initiate power iteration class
        powerIteration = PowerIteration()
        # run until there is no more teleportations, meaning it is finished
        run = True
        while run:
            powerIteration.setMatrix(self.matrix)
            self.matrix = powerIteration.run()
            if self.matrix is None:
                run = False
