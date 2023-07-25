import cv2

cv2.namedWindow('new',cv2.WINDOW_NORMAL)

cv2.imshow('new',0)

cv2.resizeWindow('new',1920,1080)

key = cv2.waitKey(0)
if(key == 'q'):
    exit()


cv2.destroyAllWindows
