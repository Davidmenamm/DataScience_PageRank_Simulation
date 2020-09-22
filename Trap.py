# Class to manage traps of the power iteration algorithm
# Receives: vector to test
# Returns: name of corresponding trap or 'None' if none
# Manages spider traps occupying up to 20% of the number of nodes

# imports
import numpy as np
import math


class Trap:
    # constructor
    def __init__(self):
        # atributes
        self.vector = None
        self.minValue = 0.05
        self.factorForSTrap = 0.4

    # to make numpy matrix-vector, one dimensional
    def vector1D(self, vector):
        newVect = np.array([])
        for i in vector:
            newVect = np.append(newVect, i[0])
        return newVect

    # to run the algorithm
    def validate(self, vector):
        # to stop validating when already identified type of trap
        readyToReturn = False
        # to store type of trap
        typeOfTrap = 'None'
        # vector length
        vectorLen = len(vector)
        # turn vector into 1D numpy array
        vect1D = self.vector1D(vector)

        # Case it is an spider trap:
        # sort vector values in descending order
        descendingVect = -np.sort(-vect1D)
        # split vector in two, 1 containing 20% vals and the other the rest
        numOfHigherVals = math.floor(vectorLen*self.factorForSTrap)
        higherValVector, lowerValVector = np.split(
            descendingVect, [numOfHigherVals])
        # sum 20% higher and 80% lower values vectors
        sumHigher = np.sum(higherValVector)
        sumLower = np.sum(lowerValVector)
        # print(sumHigher, '**>**', 6*sumLower)
        if(sumHigher > 10*sumLower):
            typeOfTrap = 'Spider'
            readyToReturn = True

        # case its a dead end trap
        if(not readyToReturn):
            # check if all elements are below a minimum value
            count = 0
            for i in range(0, vectorLen):
                if vect1D[i] < self.minValue:
                    count += 1
                else:
                    break
            print('count', count)
            print('vectorLen', vectorLen)
            if count == vectorLen:
                typeOfTrap = 'DeadEnd'
        # Return type of trap
        return typeOfTrap
