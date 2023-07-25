import cv2
#'D:\\UUU\\XXX.JEPG' 加载路径

cv2.namedWindow('new',cv2.WINDOW_NORMAL)
img = cv2.imread('d:\\Warframe0000.jpg')

cv2.imshow('new',img) 

key = cv2.waitKey(0)
print(key)
print('q')
print(ord('q'))

if(key & 0xFF == ord('q')):
  cv2.destroyAllWindows()

 
