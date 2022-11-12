# from imageprocessing import *
# start = time.time()
# InputFolderWithCrop("sample/sampel acak")
# croppicture("sample/sampel acak/a.png","result_picture/"+str(1)+".png")
# end = time.time()
# print("The time of execution of above program is :",
# (end-start) * 10**3, "ms")

import os
from imageprocessing import *
start = time.time()
InputFolderWithCrop("test\Data_Set\pins_Anthony Mackie")
# croppicture("sample/sampel acak/a.png","result_picture/"+str(1)+".png")
end = time.time()
print("The time of execution of above program is :",(end-start) * 10**3, "ms")
