import cv2

cv2.namedWindow('new',cv2.WINDOW_NORMAL)
img = cv2.imread('d:\\Warframe0000.jpg')

cv2.imshow('new',img) 

key=cv2.waitKey(0)
if(key=='q'):
    exit()
 
cv2.destroyAllWindows()