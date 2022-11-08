from imageprocessing import *
start = time.time()
InputFolderWithCrop("sample/sampel acak")
croppicture("sample/sampel acak/a.png","result_picture/"+str(1)+".png")
end = time.time()
print("The time of execution of above program is :",
(end-start) * 10**3, "ms")