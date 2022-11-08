import cv2
 
img = cv2.imread('face.jpg', cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)
 
scale_percent = 256 # percent of original size
height1, width1, channels1 = img.shape
width = int(img.shape[1] * scale_percent / height1)
height = int(img.shape[0] * scale_percent / width1)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()