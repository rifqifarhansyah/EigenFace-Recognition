import os
import cv2
import numpy as np
from eigenfaces import *
import time
from PIL import Image

start = time.time()


# from main import *
image_input = cv2.imread("D:/ITB 21/KULYAHHH/SEMESTER 3/AlGeo/TUBES 2 ALGEO/Algeo02-21099/test/gray/CR6.png", 0)
dirDataSet = "D:/ITB 21/KULYAHHH/SEMESTER 3/AlGeo/TUBES 2 ALGEO/Algeo02-21099/test/gray"

# *** find the normalized of Data Set ***
trainingFaces = getTrainingFaces(dirDataSet)

# *** convert test image to vector ***
matrixImage = np.asarray(image_input) # NOT FIX
vectorImage = getVectorImage(matrixImage)

# *** find best Eigen Vector of DataSet ***
bestEigenVector = getBestEigenFaces(trainingFaces)

# *** find the linear combination of bestEigenVector from test image ***
linerCombination = getLinComOfEigVector(bestEigenVector, vectorImage)

# *** find matrix of coeff LinearCombination ***
matrixLinCom = getLinComMatrix(bestEigenVector, trainingFaces)
minimumDistance = getMinimumDistance(linerCombination, matrixLinCom)

# *** tolerance value ***
toleranceValue = 1

if (minimumDistance < toleranceValue) :
    imagefile = getClosestImage(dirDataSet, matrixLinCom, linerCombination)
    print(imagefile)

end = time.time()
print("The time of execution of above program is :",
(end-start) * 10**3, "ms")




