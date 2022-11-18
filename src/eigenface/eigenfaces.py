import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
from eigenface import eigen

def getBestEigenFaces(mean_subtracted) :
    """
    return matriks of the best eigenvector of covariance 
    matrix of normalizedData, with EigenVector in each column
    size : N^2 x count (count is number of best)
    """
    redCov = np.matmul(np.transpose(mean_subtracted), mean_subtracted)
    redEigenValues, allEigenVectors = eigen.getEignValuesVectors(redCov)

    # Asumsi top eigen vector berbanding lurus dengan top eigen values
    greThanOne = 0
    for i in redEigenValues :
        if i > 1 :
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
    minimum = minimum = np.linalg.norm(np.subtract(inputLinCom, np.transpose([CoefMatrix[:, 0]])))
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

# def getVectorImage(matrixImage) :
#     """
#     return vector image of Image 
#     that is reshapped matrix to single column matrix
#     size : N^2 x 1
#     """
#     numRow = len(matrixImage)
#     numCol = len(matrixImage[0])
#     Vector = np.zeros((numRow*numCol, 1))
#     count = 0
#     # print(numRow, numCol)
#     # print(type(numRow))
#     for i in range(numRow) :
#         for j in range(numCol) :
#             # print(count,i,j)
#             Vector[count][0] = matrixImage[i][j]
#             count += 1
#     return Vector

# def getImageFromVector (vectorImage) :
#     """
#     size of vectorImage : 256^2 x 1 
#     return matrix of image with size 256x256
#     correspond with vectorImage
#     """
#     imageMatrix = np.zeros((256, 256))
#     count = 0
#     for i in range(256) :
#         for j in range(256) :
#             imageMatrix[i][j] = vectorImage[count][0]
#             count += 1
#     return imageMatrix

# def getAvgFaces(Path) : 
#     """
#     return the average of vector Image of all image in dirPath
#     size : N^2 x 1
#     """
#     sumImage = np.zeros((256*256, 1))
#     count = 0
#     for (dirPath, dirNames, file) in os.walk(Path):
#         for fileNames in file :
#             count += 1
#             tempPath = os.path.join(dirPath, fileNames)
#             image = cv2.imread(tempPath, 0) # foto grayscale yang udah 256x256
#             arrayImage = np.asarray(image)
#             imageVector = getVectorImage(arrayImage)
#             sumImage = np.add(imageVector, sumImage)
    
#     averageImage = np.multiply(sumImage , (1/count))
#     return averageImage
    
# def getReducedCov (Matrix) : #
#     """
#     return reduced covariance matrix of Matrix 
#     redCov = transpose(Matrix) * Matrix
#     """
#     transposedMatrix = np.transpose(Matrix)
#     covarian = np.matmul(transposedMatrix, Matrix)
#     return covarian

# def getCov (Matrix) :
#     """
#     return covariance matrix of Matrix
#     Covariance = Matrix * transpose(Matrix) 
#     """
#     transposedMatrix = np.transpose(Matrix)
#     redCovarian = np.matmul(Matrix, transposedMatrix)
#     return redCovarian

# def getTrainingFaces(Path) : # 256^2 x count
#     """
#     return the mean-subtracted image vectors 
#     that stacked horizontally as columns
#     size : N^2 x Num
#     """
#     normalizedDataSet = np.empty((256*256,0), float)
#     average = getAvgFaces(Path)

#     for (dirPath, dirNames, file) in os.walk(Path):
#         for fileNames in file :
#             tempPath = os.path.join(dirPath, fileNames)
#             image = cv2.imread(tempPath, 0)
#             arrayImage = np.asarray(image)
#             imageVector = getVectorImage(arrayImage)
#             normalizedVector = np.subtract(imageVector, average)
#             normalizedDataSet = np.column_stack((normalizedDataSet, normalizedVector))

#     return normalizedDataSet

