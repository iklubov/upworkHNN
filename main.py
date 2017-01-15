import numpy

import loadData
import neuroModel
import utils

#load data from csv
inputData = loadData.loadData()
#count cost and p matrix
costMatrix = utils.createCostMatrix(inputData)
pMatrix = utils.createIDMatrix(inputData)
derivMatrix = utils.createZeroMatrix(inputData)

#init data and count energy
neuroModel.initNeuroModel(len(inputData), costMatrix, pMatrix, derivMatrix)

for i in range(100):
    totalEnergy = utils.countEnergy(costMatrix, pMatrix, neuroModel.OUTPUTS)
    utils.countDerivative(derivMatrix, costMatrix, pMatrix, 100)
    neuroModel.updateModelState(derivMatrix)
    #print('CYCLE %s SUMDERIVATIVES %s' % (i, numpy.sum(derivMatrix)))
