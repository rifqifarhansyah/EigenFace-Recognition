# from imageprocessing import *
# start = time.time()
# InputFolderWithCrop("sample/sampel acak")
# croppicture("sample/sampel acak/a.png","result_picture/"+str(1)+".png")
# end = time.time()
# print("The time of execution of above program is :",
# (end-start) * 10**3, "ms")

import os
from imageprocessing import *
arr=os.listdir("test//Data_Set")

cnt=1
gray("test//Data_Set//Anthony Mackie9_556.jpg","test/Data_Set_adjust"+str(cnt)+".png")
for path, currentDirectory, files in os.walk("test//Data_Set"):
        for listfile in files:
            print("test//Data_Set"+'//'+listfile)
            # gray("test//Data_Set"+'//'+listfile,"test/Data_Set_adjust"+str(cnt)+".png")
            # if(listfile[-3:]=="jpg" or listfile[-3:]=="png" or listfile[-4:]=="jpeg"):
            #     # isExist = os.path.exists(pathname+'/'+listfile)
            #     croppicture(pathname+'/'+listfile,"result_picture/"+str(cnt)+".png")
            #     cnt+=1