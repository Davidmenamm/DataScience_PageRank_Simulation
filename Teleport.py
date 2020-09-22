# Class to manage teleportations

# imports
import numpy as np


class Teleport:
    # constructor
    def __init__(self, matrix, beta):
        # atributes
        self.matrix = matrix  # current matrix, changes when teleported
        self.beta = beta

    # to check if matrix needs adjusting
    def needAdj(self):
        needAdj = False
        transpose = self.matrix.transpose()
        lenMat = len(transpose)
        count = 0
        for i in range(0, lenMat):
            if np.sum(transpose[i]) == 0:
                break
            count += 1
        if(count != lenMat):
            needAdj = True
        return needAdj

    # To adjust equal probability matrix in case of DeadEnd trap
    # Returns the indexes where there does not exist a dead end

    def adjEqMatrix(self):
        # test matrix
        transpose = self.matrix.transpose()
        notDeadEndIdxs = []
        for i in range(0, len(transpose)):
            if np.sum(transpose[i]) != 0:
                notDeadEndIdxs.append(i)
        return notDeadEndIdxs

    # to run power iteration algorithm
    def powerIterTeleport(self):
        # init eq prob matrix
        numNodes = len(self.matrix)
        eqProbMat = np.full((numNodes, numNodes), 1/numNodes)
        # calculate new teleport matrix
        gamma = 1-self.beta
        newMatrix = self.beta * self.matrix
        # sum by the corresponding eq prob matrix
        if self.needAdj():
            # which columns dont need adjusting, to multiply only them
            notDeadEnd = self.adjEqMatrix()
            # multiply necesary columns
            eqProbMat[:, notDeadEnd] = eqProbMat[:, notDeadEnd] * gamma
        else:
            eqProbMat = gamma * eqProbMat
        newMatrix += eqProbMat
        return newMatrix
