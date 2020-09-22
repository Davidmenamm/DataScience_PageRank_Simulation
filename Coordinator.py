# Class to coordinate page rank and random walker algorithm

# imports
from PowerIteration import PowerIteration
import numpy as np


class Coordinator:
    # constructor
    def __init__(self, matrix):
        # atributes
        self.matrix = matrix  # current matrix, changes when teleported

    # to run power iteration algorithm
    def runAlgorithms(self):
        # initiate power iteration class
        powerIteration = PowerIteration()
        # initial vector and matrix for power iteration
        numNodes = len(self.matrix)
        initialVector = np.full((numNodes, 1), 1/numNodes)
        powerIteration.setInit(self.matrix, initialVector)
        print('Iteration 0')
        print(initialVector.transpose())
        # run both algorithms coordinating in time t
        n = 60
        for i in range(n):
            # Print name of each iteration
            print(f'\nIteration {i+1}:')
            # Run power iteration algorithm
            newMatrix, newVector = powerIteration.run()
            # the case when it a teleport was done
            if newVector is None:
                newVector = initialVector
            # matrix and vector for next iteration
            powerIteration.setInit(newMatrix, newVector)
