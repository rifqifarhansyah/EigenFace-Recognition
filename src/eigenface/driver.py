import os
import cv2
import sys
import numpy as np
# from eigenfaces import *
from PIL import Image
from eigenface import eigenfaces


sys.path.append('')
def computeFaceRecognition(image_input):

    dirDataSet = "test/User_DataSet"

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
    toleranceValue = 2
    print(minimumDistance)
    if (minimumDistance < toleranceValue) :
        imagefile = eigenfaces.getClosestImage(dirDataSet, matrixLinCom, linerCombination)
        return(imagefile)

