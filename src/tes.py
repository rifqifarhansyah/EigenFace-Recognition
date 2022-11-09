import numpy as np

# matriks = [[1, 2, 3, 4],[4, 5, 6, 7]]
# matriksd = np.array(matriks)
# matrikss = np.array(matriks)
# # print(matriks)
# # matrikss = np.transpose(matriks)
# # print(matrikss)
# kali = np.multiply(matriks , 1/3)
# # w,v = np.linalg.eig(kali)
# print(kali)
# print(type(kali[0][0]))


# # numRow, colRow = kali.shape 
# Vector = np.zeros((170000000, 17000))
# print(type(Vector[0][0]))
# # count = -1
# # for i in range(numRow) :
# #     for j in range(colRow) :
# #         count += 1
# #         Vector[count][0] = (kali[i][j])

# # print(Vector[0][0])
# # print(type(Vector[0][0]))
arr = np.empty((2,0), float)
col = np.array([[6],
                [0]])
arr = np.column_stack((arr,col))
print(arr)