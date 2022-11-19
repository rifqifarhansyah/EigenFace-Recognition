import os
import cv2
import sys
import numpy as np
# from eigenfaces import *
from PIL import Image
from eigenface import eigenfaces

sys.path.append('')
def computeFaceRecognition(image_input,self):

    dirDataSet = "test/Input/User_DataSet"

    allImage = np.empty((256*256,0), float)
    for (dirPath, dirNames, file) in os.walk(dirDataSet):
        for fileNames in file :
                tempPath = os.path.join(dirPath, fileNames)
                image = cv2.imread(tempPath, 0) # foto grayscale yang udah 256x256
                allImage= np.column_stack((allImage, image.reshape(256*256, 1)))

    
    # *** find the normalized of Data Set ***
    mean_subtracted = allImage - allImage.mean(axis=1, keepdims=True)

    # *** convert test image to vector ***
    vectorImage = image_input.reshape(256*256, 1)
    print("processing.. 5%")

    # *** find best Eigen Vector of DataSet ***
    bestEigenFaces = eigenfaces.getBestEigenFaces(mean_subtracted)
    print("processing.. 35%")

    # *** find the linear combination of bestEigenVector from test image ***
    inputCoordinate = eigenfaces.getLinComOfEigVector(bestEigenFaces, vectorImage)

    # *** find matrix of coeff LinearCombination ***
    allImageCoordinate = eigenfaces.getLinComMatrix(bestEigenFaces, mean_subtracted)
    minimumDistance = eigenfaces.getMinimumDistance(inputCoordinate, allImageCoordinate, self)
    print("processing.. 70%")

    # *** tolerance value ***
    toleranceValue = 1
    print(minimumDistance)
    if (minimumDistance < toleranceValue) :
        imagefile = eigenfaces.getClosestImage(dirDataSet, allImageCoordinate,inputCoordinate)
        return(imagefile)
    else :
        return("image/nf.jpg")

def getTraining() :
    dirDataSet = "test/Input/User_DataSet"

    allImage = np.empty((256*256,0), float)
    for (dirPath, dirNames, file) in os.walk(dirDataSet):
        for fileNames in file :
                tempPath = os.path.join(dirPath, fileNames)
                image = cv2.imread(tempPath, 0) # foto grayscale yang udah 256x256
                allImage= np.column_stack((allImage, image.reshape(256*256, 1)))

    
    # *** find the normalized of Data Set ***

    mean_subtracted = allImage - allImage.mean(axis=1, keepdims=True)

    print("processing EigenFaces..")
    # *** find best Eigen Vector of DataSet ***
    bestEigenVector = eigenfaces.getBestEigenFaces(mean_subtracted )

    # *** find matrix of coeff LinearCombination ***
    allImageCoordinate = eigenfaces.getLinComMatrix(bestEigenVector, mean_subtracted )

    np.savetxt("test\\Input\\live\\csv_file\\MatrixLinCom.csv", allImageCoordinate, delimiter = ",")

    np.savetxt("test\\Input\\live\\csv_file\\bestEigenVector.csv", bestEigenVector, delimiter = ",")

    print("Training udah selesai")

def generateClosestImage(image_input, dirInputDataSet) :

    bestEigenVector = np.loadtxt("test\\Input\\live\\csv_file\\bestEigenVector.csv", delimiter=",", dtype=float)
    
    allImageCoordinate = np.loadtxt("test\\Input\\live\\csv_file\\MatrixLinCom.csv", delimiter = ",", dtype=float)

    # *** convert test image to vector ***
    vectorImage = image_input.reshape(256*256, 1)

    # *** find the linear combination of bestEigenVector from test image ***
    inputCoordinate = eigenfaces.getLinComOfEigVector(bestEigenVector, vectorImage)

    minimumDistance = eigenfaces.getMinimumDistance(inputCoordinate, allImageCoordinate)

    # *** tolerance value ***
    toleranceValue = 2
    print(minimumDistance)
    if (minimumDistance < toleranceValue) :
        print("dapat image")
        imagefile = eigenfaces.getClosestImage(dirInputDataSet,allImageCoordinate, inputCoordinate)
        print(imagefile)
        return(imagefile)
    else :
        print("ga dapat")
        return("image/nf.jpg")

