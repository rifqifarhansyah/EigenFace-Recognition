import numpy as np
from dummyeigen import *
import cv2
from matplotlib import pyplot as plt
import time
import sys

np.set_printoptions(threshold=sys.maxsize)
start_time = time.time()


image_input = cv2.imread("D://ITB 21//KULYAHHH//SEMESTER 3//AlGeo//TUBES 2 ALGEO//Algeo02-21099//test//Coba_coba//IMG-20221117-WA0009.jpg", 0)

dirDataSet = "D://ITB 21//KULYAHHH//SEMESTER 3//AlGeo//TUBES 2 ALGEO//Algeo02-21099//test//Input//User_DataSet"

allImage = np.empty((256*256,0), float)
for (dirPath, dirNames, file) in os.walk(dirDataSet):
    for fileNames in file :
            tempPath = os.path.join(dirPath, fileNames)
            image = cv2.imread(tempPath, 0) # foto grayscale yang udah 256x256
            allImage= np.column_stack((allImage, image.reshape(256*256, 1)))

# *** find the normalized of Data Set ***
mean_subtracted = allImage - allImage.mean(axis=1, keepdims=True)

print(np.linalg.norm(np.subtract(image_input.reshape(256*256, 1), np.transpose([allImage[:, 0]]))))

# *** convert test image to vector and centered***
# 1
vectorImageCentered = np.subtract(image_input.reshape(256*256, 1), np.transpose([allImage.mean(axis=1)]))

# print(np.linalg.norm(np.subtract(vectorImageCentered, np.transpose([mean_subtracted[:, 0]]))))

# *** find best Eigen Vector of DataSet ***
bestEigenFaces = getBestEigenFaces(mean_subtracted)
print("processing.. 35%")

# *** find the linear combination of bestEigenVector from test image ***
#2
inputCoordinate = np.linalg.lstsq(bestEigenFaces, vectorImageCentered, rcond=None)[0]
# *** find matrix of coeff LinearCombination ***
# buatDebug = np.linalg.lstsq(bestEigenFaces, np.transpose([mean_subtracted[:, 0]]), rcond=None)[0]

allImageCoordinate = np.linalg.lstsq(bestEigenFaces, mean_subtracted, rcond=None)[0]

# print(np.linalg.norm(np.subtract(inputCoordinate, np.transpose([allImageCoordinate[:, 0]]))))

minimumDistance = getMinimumDistance(inputCoordinate, allImageCoordinate)

print("processing.. 70%")

# print(np.linalg.norm(np.subtract(vectorImageCentered,np.transpose( [output]))))
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


# # vectorImage = image_input.reshape(256*256, 1)
# # print("processing.. 5%")
# fig = plt.figure(figsize=(1, 2))
# fig.add_subplot(1, 2, 1)
# plt.imshow(vectorImageCentered.reshape(256,256), 'gray')
# plt.axis('off')

# fig.add_subplot(1, 2, 2)
# plt.imshow(output.reshape(256, 256), 'gray')
# plt.axis('off')

# # fig.add_subplot(1, 3, 3)
# # plt.imshow(allImage.mean(axis=1).reshape(256, 256), 'gray')
# # plt.axis('off')
# plt.show()

