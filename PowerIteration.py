# Class to run the page rank algorithm

# imports
import numpy as np
from Trap import Trap
from Teleport import Teleport


class PowerIteration:
    # constructor
    def __init__(self):
        # atributes
        self.matrix = None
        self.vector = None
        self.beta = 0.80

    # to set new matrix
    def setInit(self, matrix, vector):
        self.matrix = matrix
        self.vector = vector

    # to ask user about teleportation
    def ask(self, typeOfTrap):
        response = input(
            f'You fell on a {typeOfTrap} Trap. Want to Teleport (Y/n)')
        selection = True if response == 'Y' else False
        return selection

    # Run the power iteration algorithm
    # Returns athe same matrix and actualized vector each time
    # When teleported returns new matrix and a None vector
    def run(self):
        vector = self.vector
        matrix = self.matrix
        # to initiate managers of traps and teleportation
        trapValidation = Trap()
        teleport = Teleport(matrix, self.beta)
        # update vector each iteration
        vector = matrix.dot(vector)
        print(vector.transpose())
        print('sum of rank vector', np.sum(vector))
        # validate traps
        typeOfTrap = trapValidation.validate(vector)
        # Let user choose if they want to teleport
        if(typeOfTrap != 'None'):
            response = self.ask(typeOfTrap)
            if(response):
                matrix = teleport.powerIterTeleport()
                vector = None

        return matrix, vector
