import os
import cv2
import sys
import numpy as np
# from eigenfaces import *
from PIL import Image
from eigenface import eigenfaces

sys.path.append('')
def computeFaceRecognition(image_input):

    dirDataSet = "test/Input/User_DataSet"

    # *** find the normalized of Data Set ***
    trainingFaces = eigenfaces.getTrainingFaces(dirDataSet)

    # *** convert test image to vector ***
    matrixImage = np.asarray(image_input) 
    vectorImage = eigenfaces.getVectorImage(matrixImage)
    print("processing.. 5%")

    # *** find best Eigen Vector of DataSet ***
    bestEigenVector = eigenfaces.getBestEigenFaces(trainingFaces)
    print("processing.. 35%")

    # *** find the linear combination of bestEigenVector from test image ***
    linerCombination = eigenfaces.getLinComOfEigVector(bestEigenVector, vectorImage)

    # *** find matrix of coeff LinearCombination ***
    matrixLinCom = eigenfaces.getLinComMatrix(bestEigenVector, trainingFaces)
    minimumDistance = eigenfaces.getMinimumDistance(linerCombination, matrixLinCom)
    print("processing.. 70%")

    # *** tolerance value ***
    toleranceValue = 1
    print(minimumDistance)
    if (minimumDistance < toleranceValue) :
        imagefile = eigenfaces.getClosestImage(dirDataSet, matrixLinCom, linerCombination)
        return(imagefile)
    else :
        return("image/nf.jpg")

def getTraining() :
    dirDataSet = "test/Input/User_DataSet"

    # *** find the normalized of Data Set ***
    trainingFaces = eigenfaces.getTrainingFaces(dirDataSet)

    # *** find best Eigen Vector of DataSet ***
    bestEigenVector = eigenfaces.getBestEigenFaces(trainingFaces)

    # *** find matrix of coeff LinearCombination ***
    matrixLinCom = eigenfaces.getLinComMatrix(bestEigenVector, trainingFaces)

    np.savetxt("test\\Input\\live\\csv_file\\MatrixLinCom.csv", matrixLinCom,
              delimiter = ",")

    np.savetxt("test\\Input\\live\\csv_file\\bestEigenVector.csv", bestEigenVector,
              delimiter = ",")
    print("Training udah selesai")

def generateClosestImage(image_input) :
    dirDataSet = "test/Input/User_DataSet"

    bestEigenVector = np.loadtxt("test\\Input\\live\\csv_file\\bestEigenVector.csv", delimiter=",", dtype=float)
    
    matrixLinCom = np.loadtxt("test\\Input\\live\\csv_file\\MatrixLinCom.csv", delimiter = ",", dtype=float)

    # *** convert test image to vector ***
    matrixImage = np.asarray(image_input)
    vectorImage = eigenfaces.getVectorImage(matrixImage)

    # *** find the linear combination of bestEigenVector from test image ***
    linerCombination = eigenfaces.getLinComOfEigVector(bestEigenVector, vectorImage)

    minimumDistance = eigenfaces.getMinimumDistance(linerCombination, matrixLinCom)

    # *** tolerance value ***
    toleranceValue = 1
    print(minimumDistance)
    if (minimumDistance < toleranceValue) :
        print("dapat image")
        imagefile = eigenfaces.getClosestImage(dirDataSet, matrixLinCom, linerCombination)
        return(imagefile)
    else :
        print("ga dapat")
        return("image/nf.jpg")

