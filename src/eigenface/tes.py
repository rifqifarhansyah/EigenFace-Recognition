import os
import cv2
import numpy as np
# from eigenfaces import *
from PIL import Image

from dummyeigen import *
import time

# displayEigenFaces ()
start_time = time.time()



# Path = "D:/ITB 21/KULYAHHH/SEMESTER 3/AlGeo/TUBES 2 ALGEO/Algeo02-21099/test/Coba_coba/gray"

# normalizedDataSet = np.empty((256*256,0), float)
# for (dirPath, dirNames, file) in os.walk(Path):
#         for fileNames in file :
#                 tempPath = os.path.join(dirPath, fileNames)
#                 image = cv2.imread(tempPath, 0) # foto grayscale yang udah 256x256
#                 normalizedDataSet = np.column_stack((normalizedDataSet, image.reshape(256*256, 1)))

# print(normalizedDataSet)

# my_matrix = np.array([[1, 2, 3, 4], [1, 1, 1, 1]])
# matrix_rows_average = my_matrix - my_matrix.mean(axis=1, keepdims=True)
# print(matrix_rows_average)
# displayEigenFaces ()

best_eigen = np.array([[1, 2, 3, 4], 
                      [12, 6, 2, 8],
                      [17, 10.5, 8, 12]])
# wow = np.empty((3, 0))
allImage = np.array([[5, 8 , 9, 52, 41],
                    [29, 182, 15, 219, 318],
                    [21, 31, 29, 37, 43]])
# matrix = np.array([7, 4,2])
# hasil = np.subtract(np.transpose([allImage]), np.transpose([matrix]))
# hasil = best_eigen.mean(axis=1)
hasil = np.matmul(best_eigen, (np.linalg.lstsq(best_eigen, allImage, rcond=None)[0]))
# array = np.array([[1], [12], [17]])

# hasil = np.transpose([allImage.mean(axis=1)])
# hasil = np.linalg.norm(np.subtract(array, np.transpose([allImage[:,0]])))
print(hasil)

# my_matrix = np.array([[3], [8]])
# redEigenValues, allEigenVectors = np.linalg.eig(my_matrix)
# print(redEigenValues)
# print(allEigenVectors)
# print(np.transpose(my_matrix))
# average = getAvgFaces("D:/ITB 21/KULYAHHH/SEMESTER 3/AlGeo/TUBES 2 ALGEO/Algeo02-21099/test/Coba_coba/gray")
# dirDataSet = "D:/ITB 21/KULYAHHH/SEMESTER 3/AlGeo/TUBES 2 ALGEO/Algeo02-21099/test/Coba_coba/gray"

# *** find the normalized of Data Set ***
# trainingFaces = getTrainingFaces(dirDataSet)
# redCov = getReducedCov(trainingFaces)
# redEigenValues, allEigenVectors = getEignValuesVectors(redCov)
# *** convert test image to vector ***
# matrixImage = np.asarray(image_input) 
# vectorImage = eigenfaces.getVectorImage(matrixImage)

end_time = time.time()
print("execution time : ",end_time-start_time, " detik")
# # print(average)
# plt.imshow(getImageFromVector(average), cmap='gray')
# plt.show()


# fig = plt.figure(figsize=(1,1))
# rows = 1
# columns = 1
# image_input = cv2.imread("D://ITB 21//KULYAHHH//SEMESTER 3//AlGeo//TUBES 2 ALGEO//Algeo02-21099//test//Coba_coba//gray//CR56.png",0)
# bestEigenVector = np.loadtxt("test\\Input\\live\\csv_file\\bestEigenVector.csv", delimiter=",", dtype=float)
# image = getImageFromVector(np.transpose([bestEigenVector[:,0]]))
# hori = np.concatenate((image_input, image), axis=1)
# verti = np.concatenate((image_input, image), axis=0)
# cv2.imshow('horizontal', hori)
# cv2.imshow('vertical',verti)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# fig.add_subplot(rows, columns, 1)

# imgplot =plt.imshow(image_input)
# plt.show()


