import os
from imageprocessing import *
from PIL import Image
import numpy as np

img=Image.open("test\Coba_coba\Data_Set\pins_Alex Lawther\Alex Lawther5_120.jpg")
numpydata=np.asarray(img)
print(numpydata.shape)
imgres=adjustOneImage(numpydata)
# img2=cv2.imread("test\Coba_coba\Data_Set\pins_Alex Lawther\Alex Lawther5_120.jpg")
# print(img2.shape)
# print(img2.shape)
# img3=adjustOneImage(img2)
# img2=adjustOneImage("D:\\ITB 21\KULYAHHH\SEMESTER 3\AlGeo\TUBES 2 ALGEO\Algeo02-21099\\test\Input\\612.png")
# cv2.imshow("ass",img2)
# print(cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY))
# print(img2)
# print(type(img))
# print(type(img2))
# print(img.shape())
# res=adjustOneImage(img)
# cv2.imshow("hasil",res)
# InputFolderWithoutCrop("test/Data_set/pins_amber heard","test/User_Dataset")
# deleteFileinFolder("test\Coba_coba\kita")
# deleteFileinFolder("test\\Input\\User_DataSet")
# InputFolderWithoutCrop("D:\\fotoriz")
# InputFolderWithoutCrop()
# arr=os.listdir("test//Data_Set")
# print(arr)
# # image=cv2.imread("D:\Kuliah\Semester 3\IF2123 Aljabar Linier dan Geometri\Algeo02-21099\\test\Data_Set\pins_Anne Hathaway\Anne Hathaway82_482.jpg")
# cnt=1
# for i in arr :
#     # print("test//Data_Set"+str(i))
#     for path, currentDirectory, files in os.walk("test/Data_Set/"+str(i)):
#             for listfile in files:
#                 print("test\Data_Set\\"+str(i)+"\\"+listfile)
#                 image=cv2.imread("test\Data_Set\\"+str(i)+"\\"+listfile)
#                 gray("test\Data_Set\\"+str(i)+"\\"+listfile,"test/Data_set_adjust/"+str(cnt)+".png")
#                 cnt=cnt+1
#             # if(listfile[-3:]=="jpg" or listfile[-3:]=="png" or listfile[-4:]=="jpeg"):
#                 # isExist = os.path.exists(pathname+'/'+listfile)
#                 # croppicture(pathname+'/'+listfile,"result_picture/"+str(cnt)+".png")
#                 # cnt+=1