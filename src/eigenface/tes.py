import argparse
import cv2
import os
import numpy as np

from eigenfaces import *
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

p = np.array([2,3,4,5,7])
q = np.array([[2, 4, 3, 7, 8], [6, 5, 4, 2, 3], [3, 5, 9, 7, 8],[0,6,2,7,5],[0,0,0,0,0]])

print(np.linalg.solve(q, p))