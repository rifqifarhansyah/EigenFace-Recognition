import os
import cv2
import numpy as np
from eigenfaces import *
import time
start = time.time()
end = time.time()
print("The time of execution of above program is :",
(end-start) * 10**3, "ms")


# from main import *
image_input = cv2.imread("D:/ITB 21/KULYAHHH/SEMESTER 3/AlGeo/TUBES 2 ALGEO/Algeo02-21099/test/gray/CR6.png", 0)
dirDataSet = "D:/ITB 21/KULYAHHH/SEMESTER 3/AlGeo/TUBES 2 ALGEO/Algeo02-21099/test/gray"

# *** find the normalized of Data Set ***
trainingFaces = getTrainingFaces(dirDataSet)
print("masuk sini")
# *** convert test image to vector ***
matrixImage = np.asarray(image_input) # NOT FIX
vectorImage = getVectorImage(matrixImage)
print("udah here")
# *** find best Eigen Vector of DataSet ***
bestEigenVector = getBestEigenFaces(trainingFaces)
print("anjayy")
# *** find the linear combination of bestEigenVector from test image ***
linerCombination = getLinComOfEigVector(bestEigenVector, vectorImage)
print("woyyy")
# *** find matrix of coeff LinearCombination ***
matrixLinCom = getLinComMatrix(bestEigenVector, trainingFaces)
minimumDistance = getMinimumDistance(linerCombination, matrixLinCom)
print("bismillah")

# *** tolerance value ***
toleranceValue = 1

if (minimumDistance < toleranceValue) :
    print("asoyy")
    imagefile = getClosestImage(dirDataSet, matrixLinCom, linerCombination)

    print(imagefile)

end = time.time()
print("The time of execution of above program is :",
(end-start) * 10**3, "ms")




