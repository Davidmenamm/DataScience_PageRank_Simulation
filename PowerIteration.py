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
        self.beta = 0.80

    # to set new matrix
    def setMatrix(self, matrix):
        self.matrix = matrix

    # to ask user about teleportation
    def ask(self, typeOfTrap):
        response = input(
            f'You fell on a {typeOfTrap} Trap. Want to Teleport (Y/n)')
        selection = True if response == 'Y' else False
        return selection

    # to run the algorithm
    # Receives no arguments
    # Returns a new matrix when teleported or None when the algorithm ends
    def run(self):
        # calculate inital values
        numNodes = len(self.matrix)
        initialVector = np.full((numNodes, 1), 1/numNodes)
        # to initiate managers of traps and teleportation
        trapValidation = Trap()
        teleport = Teleport(self.matrix, self.beta)
        # necesary initial prints
        print('iteration 0')
        print(initialVector.transpose())
        # to store new matrix when teleported
        newMatrix = None
        # run the algorithm for n iterations
        n = 60
        for i in range(n):
            # Respective necesary prints
            print(f'\niteration {i+1}')
            # update vector each iteration
            initialVector = self.matrix.dot(initialVector)
            print(initialVector.transpose())
            print('sum of rank vector', np.sum(initialVector))
            # validate traps
            typeOfTrap = trapValidation.validate(initialVector)
            # Let user choose if they want to teleport
            if(typeOfTrap != 'None'):
                response = self.ask(typeOfTrap)
                if(response):
                    newMatrix = teleport.powerIterTeleport()
                    break
        return newMatrix
