import os
import cv2
import numpy as np
from eigenfaces import *
from PIL import Image


# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image")
# args = vars(ap.parse_args())
# Path = "D:/ITB 21/KULYAHHH/SEMESTER 3/AlGeo/TUBES 2 ALGEO/Algeo02-21099/test/Data_Set"

# for (dirPath, dirNames, file) in os.walk(Path):
#     for fileNames in file :
#         tempPath = os.path.join(dirPath, fileNames)
#         img = cv2.imread(tempPath, 0)
#         matrix = np.asarray(img)
#         print(matrix)

        # print(getVectorImage(matrix))
        # break
        # matrix = np.asarray(img)
        # print(matrix)
        # vector = getVectorImage(matrix)
        # printf(vector)
        
# img = cv2.imread(r"D:\ITB 21\KULYAHHH\SEMESTER 3\AlGeo\TUBES 2 ALGEO\Algeo02-21099\test\gray\CR1.png", 0)
# print(img.shape)

# p = np.array([2,3,4,5,7])
# q = np.array([[2, 4, 3, 7], [6, 5, 4, 2], [3, 5, 9, 7], [3, 2, 5, 5], [4,2,5,6]])
# print(q[:,:3])

# x = np.linalg.lstsq(q, p)[0]
# print(x)
# hasil = np.zeros((5,1))
# print(hasil)
# for i in range(4) :
#     temp = np.multiply(np.transpose([q[:,i]]), x[i])
#     print(temp)
#     hasil =  np.add(hasil, temp) 

# print(hasil)

# print(getMagnitude(np.transpose([p])))

# C = np.zeros((3,3))
# A = np.array([[1,0,0],[1,4,1],[0,0,1]])
# b = np.array([0,24,0])
# x = 2
# count = 0
# for i in range(1) :
#     C[i][i] = A[1][count]

# print(C[0][0])
# print(np.transpose([A[:,0]]))

import time
start_time = time.time()



# image_input = cv2.imread("test/Input/593.png.png", 0)
# dirDataSet = "test/Input/Input_DataSet"

# # *** find the normalized of Data Set *** 
# trainingFaces = eigenfaces.getTrainingFaces(dirDataSet)

# # *** convert test image to vector ***
# matrixImage = np.asarray(image_input) # NOT FIX
# vectorImage = eigenfaces.getVectorImage(matrixImage)
# print("processing.. 5%")

# # *** find best Eigen Vector of DataSet ***
# bestEigenVector = eigenfaces.getBestEigenFaces(trainingFaces)
# print("processing.. 35%")

# # *** find the linear combination of bestEigenVector from test image ***
# linerCombination = eigenfaces.getLinComOfEigVector(bestEigenVector, vectorImage)

# # *** find matrix of coeff LinearCombination ***
# matrixLinCom = eigenfaces.getLinComMatrix(bestEigenVector, trainingFaces)
# minimumDistance = eigenfaces.getMinimumDistance(linerCombination, matrixLinCom)
# print("processing.. 95%\n")

# # matrixLinCom.tofile('test2.dat')
# np.savetxt("data3.csv", matrixLinCom,
#               delimiter = ",")

# # *** tolerance value ***
# toleranceValue = 2
# print(f"the minimum distance : {minimumDistance} \n")
# print(f"The closest image filepath : ")
# if (minimumDistance < toleranceValue) :
#         imagefile = eigenfaces.getClosestImage(dirDataSet, matrixLinCom, linerCombination)
#         print(imagefile)

end_time = time.time()

print("\ntime execution : ", (end_time-start_time) * 10**3)

# window_name = 'image'
# cv2.imshow(window_name, imagefile)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



