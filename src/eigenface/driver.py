import os
import cv2
import sys
import time
import numpy as np
# from eigenfaces import *
from PIL import Image
from eigenface import eigenfaces

sys.path.append('')
def computeFaceRecognition(image_input, dirInputDataSet):
    start_training = time.time()
    dirDataSet = "test/Input/User_DataSet"

    allImage = np.empty((256*256,0), float)
    for (dirPath, dirNames, file) in os.walk(dirDataSet):
        for fileNames in file :
            tempPath = os.path.join(dirPath, fileNames)
            image = cv2.imread(tempPath, 0) # foto grayscale yang udah 256x256
            allImage= np.column_stack((allImage, image.reshape(256*256, 1)))

    
    # *** find the normalized of Data Set ***

    mean_subtracted = allImage - allImage.mean(axis=1, keepdims=True)

    print("\nprocessing EigenFaces..")
    # *** find best Eigen Vector of DataSet ***
    start_eigen = time.time()

    bestEigenFaces = eigenfaces.getBestEigenFaces(mean_subtracted)

    end_eigen = time.time()
    print("waktu mencari eigen :", end_eigen-start_eigen)

    # *** find matrix of coeff LinearCombination ***
    allImageCoordinate = np.linalg.lstsq(bestEigenFaces, mean_subtracted, rcond=None)[0]
    # allImageCoordinate = eigenfaces.getLinComMatrix(bestEigenFaces, mean_subtracted)
    end_training = time.time()
    print("Training udah selesai")
    print("waktu training :", end_training-start_training)
    
    # *** convert test image to vector ***
    vectorImage = np.subtract(image_input.reshape(256*256, 1), np.transpose([allImage.mean(axis=1)]))

    # *** find the linear combination of bestEigenVector from test image ***
    # inputCoordinate = eigenfaces.getLinComOfEigVector(bestEigenVector, vectorImage)
    inputCoordinate = np.linalg.lstsq(bestEigenFaces, vectorImage, rcond=None)[0]

    minimumDistance = eigenfaces.getMinimumDistance(inputCoordinate, allImageCoordinate)
    print(minimumDistance)

    # *** tolerance value ***
    toleranceValue = 1
    imagefile = eigenfaces.getClosestImage(dirInputDataSet,allImageCoordinate, inputCoordinate)
    print(imagefile)
    # print(inputCoordinate)
    # print(eigenFace)
    if (minimumDistance < toleranceValue) :
        print("dapat image")
        return(imagefile)
    else :
        print("ga dapat")
        return("image/nf.jpg")

def getTraining() :
    start_training = time.time()
    dirDataSet = "test/Input/User_DataSet"

    allImage = np.empty((256*256,0), float)
    for (dirPath, dirNames, file) in os.walk(dirDataSet):
        for fileNames in file :
            tempPath = os.path.join(dirPath, fileNames)
            image = cv2.imread(tempPath, 0) # foto grayscale yang udah 256x256
            allImage= np.column_stack((allImage, image.reshape(256*256, 1)))

    
    # *** find the normalized of Data Set ***

    mean_subtracted = allImage - allImage.mean(axis=1, keepdims=True)

    print("\nprocessing EigenFaces..")
    # *** find best Eigen Vector of DataSet ***
    start_eigen = time.time()

    bestEigenFaces = eigenfaces.getBestEigenFaces(mean_subtracted)

    end_eigen = time.time()
    print("waktu mencari eigen :", end_eigen-start_eigen)

    # *** find matrix of coeff LinearCombination ***
    allImageCoordinate = np.linalg.lstsq(bestEigenFaces, mean_subtracted, rcond=None)[0]
    # allImageCoordinate = eigenfaces.getLinComMatrix(bestEigenFaces, mean_subtracted)

    np.savetxt("test\\Input\\live\\csv_file\\faceSpaces.csv", allImageCoordinate, delimiter = ",")

    np.savetxt("test\\Input\\live\\csv_file\\bestEigenFaces.csv", bestEigenFaces, delimiter = ",")
    end_training = time.time()
    print("Training udah selesai")
    print("waktu training :", end_training-start_training)
    return np.transpose([allImage.mean(axis=1)])

def generateClosestImage(image_input, dirInputDataSet, averageImage) :

    bestEigenFaces = np.loadtxt("test\\Input\\live\\csv_file\\bestEigenFaces.csv", delimiter=",", dtype=float)
    
    allImageCoordinate = np.loadtxt("test\\Input\\live\\csv_file\\faceSpaces.csv", delimiter = ",", dtype=float)

    # *** convert test image to vector ***
    vectorImage = np.subtract(image_input.reshape(256*256, 1), averageImage)

    # *** find the linear combination of bestEigenVector from test image ***
    # inputCoordinate = eigenfaces.getLinComOfEigVector(bestEigenVector, vectorImage)
    inputCoordinate = np.linalg.lstsq(bestEigenFaces, vectorImage, rcond=None)[0]

    minimumDistance = eigenfaces.getMinimumDistance(inputCoordinate, allImageCoordinate)
    print(minimumDistance)

    # *** tolerance value ***
    toleranceValue = 1
    imagefile = eigenfaces.getClosestImage(dirInputDataSet,allImageCoordinate, inputCoordinate)
    print(imagefile)
    # print(inputCoordinate)
    # print(eigenFace)
    if (minimumDistance < toleranceValue) :
        print("dapat image")
        return(imagefile)
    else :
        print("ga dapat")
        return("image/nf.jpg")

