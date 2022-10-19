import numpy as np
import math


def sigmoid_one(val):
    return 1/(1+math.exp(-val))

def dSigmoid_one(val):
    return (sigmoid_one(val)*(1-sigmoid_one(val)))

def dReLU_one(val):
    return val > 0

class activations:

    @staticmethod
    def sigmoid(val):
        sVal = []
        for y in range(val.shape[0]):
            row = []
            for x in range(val.shape[1]):
                row.append(sigmoid_one(val[y][x]))
            sVal.append(row)

        return np.array(sVal)
    
    @staticmethod
    def dSigmoid (val):
        sVal = []
        for y in range(val.shape[0]):
            row = []
            for x in range(val.shape[1]):
                row.append(dSigmoid_one(val[y][x]))
            sVal.append(row)

        return np.array(sVal)

    @staticmethod
    def ReLU (val):
        return np.maximum(0,val)

    @staticmethod
    def dReLU (val):
        sVal = []
        for y in range(val.shape[0]):
            row = []
            for x in range(val.shape[1]):
                row.append(dReLU_one(val[y][x]))
            sVal.append(row)

        return np.array(sVal)
