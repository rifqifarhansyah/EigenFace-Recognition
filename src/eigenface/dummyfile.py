import numpy as np
from dummyeigen import *
import cv2
image_input = cv2.imread("D://ITB 21//KULYAHHH//SEMESTER 3//AlGeo//TUBES 2 ALGEO//Algeo02-21099//test//Coba_coba//gray//CR56.png", 0)
import time
start_time = time.time()
dirDataSet = "test//Coba_coba//gray"

# *** find the normalized of Data Set ***
trainingFaces = getTrainingFaces(dirDataSet)
print("processing.. 5%")
# *** find best Eigen Vector of DataSet ***
bestEigenVector = getBestEigenFaces(trainingFaces)

# *** find matrix of coeff LinearCombination ***
matrixLinCom = getLinComMatrix(bestEigenVector, trainingFaces)

np.savetxt("test\\Input\\live\\csv_file\\MatrixLinCom.csv", matrixLinCom,
            delimiter = ",")

np.savetxt("test\\Input\\live\\csv_file\\bestEigenVector.csv", bestEigenVector,
            delimiter = ",")
print("Training udah selesai")

bestEigenVectorRRR = np.loadtxt("test\\Input\\live\\csv_file\\bestEigenVector.csv", delimiter=",", dtype=float)

matrixLinComRRR = np.loadtxt("test\\Input\\live\\csv_file\\MatrixLinCom.csv", delimiter = ",", dtype=float)

# *** convert test image to vector ***
matrixImage = np.asarray(image_input) 
vectorImage = getVectorImage(matrixImage)

# *** find the linear combination of bestEigenVector from test image ***
linerCombination = getLinComOfEigVector(bestEigenVectorRRR, vectorImage)

minimumDistance = getMinimumDistance(linerCombination, matrixLinComRRR)

# *** tolerance value ***
toleranceValue = 1
print(minimumDistance)
if (minimumDistance < toleranceValue) :
    print("dapat image")
    imagefile = getClosestImage(dirDataSet, matrixLinCom, linerCombination)
    print(imagefile)
else :
    print("ga dapat")

end_time = time.time()
print("time processing = ", end_time-start_time)


