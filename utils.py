import math
import numpy

from loadData import Node
from neuroModel import T1,T2,T3

# cost matrix defines as a distance btw nodes
def createCostMatrix(model):
    i = 0
    result = numpy.zeros([len(model), len(model)])
    while i < len(model):
        for index,item in enumerate(model):
            result[i,index] = result[index,i] = Node.distance(model[i], item)
        i+=1
    print('COST MATRIX CREATED \n', result)
    return result

# defines as id matrix cuz nodes have connection to each other
def createPMatrix(model):
    result = numpy.identity(len(model))
    return result


def countEnergy(costMatrix, pMatrix, vMatrix):
    cSum = countEnergySum(costMatrix, vMatrix)
    pSum = countEnergySum(pMatrix, vMatrix)
    vSum = countWeightsInEnergy(vMatrix)
    print('ENERGY COSTSUM=%s PSUM=%s MIRRORVSUM=%s' % (cSum, pSum, vSum))
    return T1/2*cSum + T2/2*pSum + T3/2*vSum
    pass


def countEnergySum(matrix1, matrix2):
    result = 0
    for i in range(len(matrix1)-1):
        for j in range(len(matrix2)-1):
            if i==j: continue
            result += matrix1[i][j] * matrix2[i,j]
    return result


def countWeightsInEnergy(matrix):
    dim = len(matrix)
    result = 0
    for i in range(dim - 1):
        sumStr = sum([matrix[i][j] for j in range(dim - 1) if j!=i])
        sumCol = sum([matrix[j][i] for j in range(dim - 1) if j!=i])
        result += math.pow(sumStr - sumCol, 2)
    return result

