import loadData
import neuroModel
import utils

#load data from csv
inputData = loadData.loadData()
#count cost and p matrix
costMatrix = utils.createCostMatrix(inputData)
pMatrix = utils.createPMatrix(inputData)

#init data and count energy
neuroModel.initNeuroModel(len(inputData), costMatrix, pMatrix)
totalEnergy = utils.countEnergy(costMatrix, pMatrix, neuroModel.OUTPUTS)
