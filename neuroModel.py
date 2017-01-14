import math

import numpy

DIMENSION = 0
BIASES = []
WEIGHTS = []
INPUTS,OUTPUTS = [],[]
T1,T2,T3,T4 = 1,2,4,8
GAIN = 1

def initNeuroModel(dimension, cmatrix, pmatrix):
    global BIASES, WEIGHTS, DIMENSION, INPUTS, OUTPUTS
    DIMENSION = dimension
    BIASES = numpy.zeros([dimension, dimension])
    INPUTS = numpy.zeros([dimension, dimension])
    OUTPUTS = numpy.ones([dimension, dimension])
    WEIGHTS = numpy.zeros([dimension, dimension, dimension, dimension])
    for i in range(dimension-1):
        for j in range(dimension-1):
            BIASES[i][j] = calculateBias(i,j,cmatrix[i][j], pmatrix[i][j])
            for k in range(dimension - 1):
                for l in range(dimension - 1):
                    WEIGHTS[i][j][k][l] = calculateWeight(i,j,k,l)
    updateModelState()

def updateModelState():
    global INPUTS, OUTPUTS, DIMENSION
    for i in range(DIMENSION - 1):
        for j in range(DIMENSION - 1):
            INPUTS[i][j] = BIASES[i][j] + multInputWeight(i,j)
            OUTPUTS[i][j] = expoutput(INPUTS[i][j])
    print(INPUTS, OUTPUTS)

def expoutput(inputValue):
    return 1.0/(1+math.exp(-GAIN*inputValue))

def multInputWeight(i,j):
    global DIMENSION
    result = sum([OUTPUTS[i,k]*WEIGHTS[i][j][i][k] for k in range(DIMENSION - 1) if j != k])
    return result

def calculateWeight(x1,y1,x2,y2):
    return -T3 * cron(x1, x2) - T3 * cron(y1, y2) + T3 * cron(x1, y2) + T3 * cron(y1, x2) + T4 * cron(x1, x2) * cron(y1, y2)

def calculateBias(x,y,c,p):
    return -T1/2*c * cron(x, y) * cron(x, y) - T2 / 2 * p * cron(x, y) - T4 / 2

def cron(a, b):
    return 1 if a==b else 0



