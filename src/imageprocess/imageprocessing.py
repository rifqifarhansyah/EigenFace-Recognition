import cv2
import os
import time

def croppicture(path,output): #input picture dengan wajah belum di crop
    img = cv2.imread(path)
    
    # Load the cascade
    # gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('src/etc/haarcascade_frontalface_alt2.xml')
    
    # Detect faces
    faces = face_cascade.detectMultiScale(img, 1.1, 4)
    
    # Draw rectangle around the faces and crop the faces
    for (x, y, w, h) in faces:
        faces = img[y:y + h, x:x + w]
        faces = cv2.cvtColor(faces, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(output, faces)

def gray(path,output): # menjadikan gambar menjadi grayscale dan resize
    image = cv2.imread(path)

    scale_percent = 256 # percent of original size
    width = int(image.shape[1] * scale_percent / image.shape[1])
    height = int(image.shape[0] * scale_percent / image.shape[0])
    dim = (width, height)
    image=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
    # print(dimensions)

    # Use the cvtColor() function to grayscale the image
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    cv2.imwrite(output,gray_image)
    

def InputFolderWithoutCrop(path): #input folder dengan wajah sudah di crop
    # return all files as a list
    cnt=1
    pathname=path
    lis=[]
    # print(pathname)
    
    for path, currentDirectory, files in os.walk(path):
        for listfile in files:
            # print(pathname+"\\"+listfile)

            if(listfile[-3:]=="jpg" or listfile[-3:]=="png" or listfile[-4:]=="jpeg"):
                # isExist = os.path.exists(pathname+'/'+listfile)
                gray(pathname+"\\"+listfile,"test/Data_set_adjust/"+str(cnt)+".png")
                cnt+=1


def InputFolderWithCrop(path): #input folder dengan wajah sudah di crop
    # return all files as a list
    cnt=1
    pathname=path
    lis=[]
    # print(pathname)
    #apabila wajah belum di crop
    for path, currentDirectory, files in os.walk(path):
        for listfile in files:
            # print(pathname+"\\"+listfile)

            if(listfile[-3:]=="jpg" or listfile[-3:]=="png" or listfile[-4:]=="jpeg"):
                # isExist = os.path.exists(pathname+'/'+listfile)
                croppicture(pathname+"\\"+listfile,"test/Data_set_adjust/"+str(cnt)+".png")
                cnt+=1

def getCroppedPicture(path) :
    img = cv2.imread(path)
    
    # Load the cascade
    # gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('src/etc/haarcascade_frontalface_alt2.xml')
    
    # Detect faces
    faces = face_cascade.detectMultiScale(img, 1.1, 4)
    
    # Draw rectangle around the faces and crop the faces
    for (x, y, w, h) in faces:
        faces = img[y:y + h, x:x + w]
        faces = cv2.cvtColor(faces, cv2.COLOR_BGR2GRAY)
    
    return faces