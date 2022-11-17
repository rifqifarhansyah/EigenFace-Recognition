import os
from imageprocessing import *
<<<<<<< HEAD
# InputFolderWithoutCrop("test/Data_set/pins_amber heard","test/User_Dataset")
# deleteFileinFolder("test\Coba_coba\kita")
# deleteFileinFolder("test\\Input\\User_DataSet")
InputFolderWithCrop("D:\\fotoriz","D:\\resfoto")
=======
deleteFileinFolder("test\Coba_coba\kita")
>>>>>>> b4764ba03cc8e4c9223eff300679aac91477c4f2
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