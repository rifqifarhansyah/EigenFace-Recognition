import numpy as np
from dummyeigen import *
import cv2
import time

start_time = time.time()


image_input = cv2.imread("D:/ITB 21/KULYAHHH/SEMESTER 3/AlGeo/TUBES 2 ALGEO/Algeo02-21099/test/Input/User_DataSet/1.png", 0)

dirDataSet = "D://ITB 21//KULYAHHH//SEMESTER 3//AlGeo//TUBES 2 ALGEO//Algeo02-21099//test//Coba_coba//DataCoba"

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
bestEigenFaces = getBestEigenFaces(mean_subtracted)
print("processing.. 35%")

# *** find the linear combination of bestEigenVector from test image ***
inputCoordinate = getLinComOfEigVector(bestEigenFaces, vectorImage)

# *** find matrix of coeff LinearCombination ***
allImageCoordinate = getLinComMatrix(bestEigenFaces, mean_subtracted)
minimumDistance = getMinimumDistance(inputCoordinate, allImageCoordinate)
print("processing.. 70%")

# *** tolerance value ***
toleranceValue = 1
print(minimumDistance)
if (minimumDistance < toleranceValue) :
    imagefile = getClosestImage(dirDataSet, allImageCoordinate,inputCoordinate)
    print(imagefile)
else :
    print("image/nf.jpg")

end_time = time.time()
print("time processing = ", end_time-start_time, " detik")


