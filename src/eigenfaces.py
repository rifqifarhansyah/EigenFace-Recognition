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
    transposedMatrix = np.transpose(Matrix)
    covarian = np.multiply(transposedMatrix, Matrix)
    return covarian

def getCov (Matrix) :
    transposedMatrix = np.transpose(Matrix)
    redCovarian = np.multiply(Matrix, transposedMatrix)
    return redCovarian

def getNormalizedDataSet(Matrix, dirPath, dirNames,) : # 256^2 x count
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



    


