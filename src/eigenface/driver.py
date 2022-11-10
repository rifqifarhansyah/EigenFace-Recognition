import os
import cv2
import numpy as np
from eigenfaces import *
from GUI.main import *

dirDataSet = "D:\\ITB 21\\KULYAHHH\\SEMESTER 3\\AlGeo\\TUBES 2 ALGEO\\Algeo02-21099\\test\\Data_Set_Adjusted"

# *** find average of DataSet ***
averageDataSet = getAverage(dirDataSet)
normalizedDataSet = getNormalizedDataSet(dirDataSet)

# *** convert test image to vector ***
matrixImage = np.asarray(image_input) # NOT FIX
vectorImage = getVectorImage(matrixImage)

# find best Eigen Vector of DataSet
bestEigenVector = getBestEigenVectors(normalizedDataSet)

# find the linear combination of bestEigenVector from test image
linerCombination = getLinComOfEigVector(bestEigenVector, vectorImage)

# find matrix of coeff LinearCombination
matrixLinCom = getLinComMatrix(bestEigenVector, normalizedDataSet)
minimumDistance = getMinimumDistance(linerCombination, matrixLinCom)

# find the closest image
order = getClosestImageOrder(linerCombination, matrixLinCom)

# tolerance value
toleranceValue = 1

if (minimumDistance < toleranceValue) :
    imagefile = getClosestImage(dirDataSet, order)








