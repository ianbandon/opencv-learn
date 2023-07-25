import cv2

#'D:\\UUU\\XXX.JEPG' 加载路径

cv2.namedWindow('new',cv2.WINDOW_NORMAL)
img = cv2.imread('d:\\Warframe0000.jpg')

while True:
    cv2.imshow('new',img) 

    key = cv2.waitKey(0)
    
    if(key & 0xFF == ord('q')):
        print('tuichu')
        break
    elif(key & 0xFF == ord('s')):
        print('baocun')
        cv2.imwrite('d:\\0000.jpg', img,)
        break
         #无损输出  cv2.imwrite('d:\\Warframe0000.jpg',img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
cv2.destroyAllWindows()