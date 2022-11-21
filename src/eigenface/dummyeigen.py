from matplotlib import pyplot as plt
import numpy as np
import time
import cv2
import os

from eigen import *

def getBestEigenFaces(mean_subtracted) :
    """
    return matriks of the best eigenvector of covariance 
    matrix of normalizedData, with EigenVector in each column
    size : N^2 x count (count is number of best)
    """
    redCov = np.matmul(np.transpose(mean_subtracted), mean_subtracted)
    start = time.time()
    redEigenValues, allEigenVectors = getEignValuesVectors(redCov)
    end = time.time()
    print("\nwaktu untuk mencari eigen value dan vector = ", end-start, " detik\n")
    # Asumsi top eigen vector berbanding lurus dengan top eigen values
    greThanOne = 0
    for i in redEigenValues :
        if i > 1 :
            print("Eigen values : ", i)
            greThanOne += 1

    redEigenVectors = allEigenVectors[:, :greThanOne]
    bestEigenVectorsOfCov = np.empty((256*256, 0), float)
    for i in range(len(redEigenVectors[0])) :
        temp = np.matmul(mean_subtracted, np.transpose([redEigenVectors[:, i]]))
        bestEigenVectorsOfCov = np.column_stack((bestEigenVectorsOfCov, temp))
    
    return bestEigenVectorsOfCov

def displayEigenFaces () :
    fig = plt.figure(figsize=(3, 5))
    bestEigenVector = np.loadtxt("test\\Input\\live\\csv_file\\bestEigenVector.csv", delimiter=",", dtype=float)
    for i in range(15) :
        image = (bestEigenVector[:,i]).reshape(256,256)
        fig.add_subplot(3, 5, i+1)
        plt.imshow(image)
        plt.axis('off')
        plt.title(i+1)
    plt.show()


def getLinComOfEigVector(bestEigenVectorsOfCov, imageVectorInput) :
    """
    return the linear Combination of bestEigenVectorsOfCov from imageVectorInput
    size : number of best eigenfaces x 1
    """
    x = bestEigenVectorsOfCov
    y = np.transpose(imageVectorInput)
    linCom = np.transpose([np.linalg.lstsq(x, y[0], rcond=None)[0]])
    return linCom

def getLinComMatrix(bestEigenVector, normalizedDataSet) :
    """
    return matrix with linear combination of bestEigenVector 
    from each image in dataset in each column
    size : number of best eigenface x number of dataset
    """
    CoefOfLinComMatrix = np.empty((len(bestEigenVector[0]),0), float)

    for i in range(len(normalizedDataSet[0])) :
        LinComOfNormalized = getLinComOfEigVector(bestEigenVector, np.transpose([normalizedDataSet[:,i]]))
        CoefOfLinComMatrix = np.column_stack((CoefOfLinComMatrix, LinComOfNormalized))
    
    return CoefOfLinComMatrix

def getMinimumDistance(inputLinCom, CoefMatrix) :
    """
    return minimum distance from linear combination of input image 
    and linear combination of each image in data set
    """
    minimum = np.linalg.norm(np.subtract(inputLinCom, np.transpose([CoefMatrix[:, 0]])))
    for i in range(len(CoefMatrix[0])) :
        distance = np.linalg.norm(np.subtract(inputLinCom, np.transpose([CoefMatrix[:, i]])))
        if (distance < minimum) :
            minimum = distance

    return minimum

def getClosestImage (dirPath, CoefMatrix, inputLinCom) :
    """
    return filename of closest image in dataset
    """
    minimum = np.linalg.norm(np.subtract(inputLinCom, np.transpose([CoefMatrix[:, 0]])))
    imageOrder = 1
    for i in range(len(CoefMatrix[0])) :
        distance = np.linalg.norm(np.subtract(inputLinCom, np.transpose([CoefMatrix[:, i]])))
        if (distance < minimum) :
            minimum = distance
            imageOrder = i + 1

    count = 0
    for (dirPath, dirNames, file) in os.walk(dirPath):
        for fileNames in file :
            count += 1
            if count == imageOrder :
                return os.path.join(dirPath, fileNames)