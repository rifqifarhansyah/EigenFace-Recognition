import numpy as np
import time
import cv2
import os
from imageprocess.imageprocessing import *
from eigen import *

def getVectorImage(Matrix) :
    numRow, colRow = Matrix.shape 
    Vector = np.zeros((numRow*colRow, 1))
    count = -1
    for i in range(numRow) :
        for j in range(colRow) :
            count += 1
            Vector[count][0] = Matrix[i][j]

def getAverage(dirPath) : # 256^2 x 1
    # list to store files name
    sumImage = np.zeros((256*256, 1))
    count = 0
    for (dirPath, dirNames, fileNames) in os.walk(dirPath):
        count += 1
        image = getCroppedPicture(fileNames) # foto grayscale yang udah 256x256
        arrayImage = np.asarray(image)
        imageVector = getVectorImage(arrayImage)
        sumImage = np.add(imageVector, sumImage)
    
    averageImage = np.multiply(sumImage , (1/count))
    return averageImage
    
def getReducedCov (Matrix) : #
    """
    return reducted covariance matrix of Matrix 
    redCov = transpose(Matrix) * Matrix
    """
    transposedMatrix = np.transpose(Matrix)
    covarian = np.multiply(transposedMatrix, Matrix)
    return covarian

def getCov (Matrix) :
    """
    return covariance matrix of Matrix
    Covariance = Matrix * transpose(Matrix) 
    """
    transposedMatrix = np.transpose(Matrix)
    redCovarian = np.multiply(Matrix, transposedMatrix)
    return redCovarian

def getNormalizedDataSet(dirPath) : # 256^2 x count
    """
    return matrix of normalized data set from its average
    """
    normalizedDataSet = np.empty((256*256,0), float)
    average = getAverage(dirPath)

    for (dirPath, dirNames, fileNames) in os.walk(dirPath):
        image = getCroppedPicture(fileNames)
        arrayImage = np.asarray(image)
        imageVector = getVectorImage(arrayImage)
        normalizedVector = np.subtract(imageVector, average)
        normalizedDataSet = np.column_stack((normalizedDataSet, normalizedVector))
    
    return normalizedDataSet

def getBestEigenVectors(normalizedData) :
    """
    return matriks of the best eigenvector of covariance matrix of normalizedData,
    with EigenVector in each column
    """
    redCov = getReducedCov(normalizedData)
    redEigenValues = getEigenValues(redCov, len(redCov))

    # Asumsi top eigen vector berbanding lurus dengan top eigen values
    greThanOne = 0
    for i in redEigenValues :
        if i > 1 :
            greThanOne += 1
    
    redEigenVectors = getEigenVectors(redCov, greThanOne)

    bestEigenVectorsOfCov = np.empty((256*256, 0), float)
    for i in range(len(redEigenVectors)) :
        temp = np.multiply(normalizedData, redEigenVectors[:, i])
        bestEigenVectorsOfCov = np.column_stack((bestEigenVectorsOfCov, temp))
    
    return bestEigenVectorsOfCov

def getLinComOfEigVector(bestEigenVectorsOfCov, imageVectorInput) :
    """
    return the linear Combination of bestEigenVectorsOfCov from imageVectorInput
    """
    x = np.transpose(bestEigenVectorsOfCov)
    linCom = np.transpose(np.linalg.solve(x, imageVectorInput))
    return linCom

def getLinComMatrix(bestEigenVector, normalizedDataSet) :
    """
    """
    CoefOfLinComMatrix = np.empty((len(bestEigenVector[0]),0), float)

    for i in range(len(normalizedDataSet[0])) :
        LinComOfNormalized = getLinComOfEigVector(bestEigenVector, normalizedDataSet[:,i])
        CoefOfLinComMatrix = np.column_stack((CoefOfLinComMatrix, LinComOfNormalized))
    
    return CoefOfLinComMatrix

def getMinimumDistance(inputLinCom, CoefMatrix) :
    minimum = 0
    for i in range(len(CoefMatrix[0])) :
        distance = abs(np.subtract(inputLinCom, CoefMatrix[:, i]))
        if (distance < minimum) :
            minimum = distance

    return minimum

def getClosestImageOrder(inputLinCom, CoefMatrix) :
    minimum = 0
    for i in range(len(CoefMatrix[0])) :
        distance = abs(np.subtract(inputLinCom, CoefMatrix[:, i]))
        if (distance < minimum) :
            minimum = distance
            order = i
    return order

def getClosestImage (dirPath, imageOrder) :
    count = 0
    for (dirPath, dirNames, fileNames) in os.walk(dirPath):
        count += 1
        if count == imageOrder :
            return fileNames

    


