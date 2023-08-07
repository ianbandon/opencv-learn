import cv2
import numpy as np

#setMouseCallback(winname,callback,userdata)
#callback(event,x,y,flags,userdata)  x,y 鼠标坐标 flags组合键

#鼠标回调函数
def mouse_callback(event, x , y , flags , ueserdata):
    print(event, x , y , flags , ueserdata)

#创建窗口
cv2.namedWindow('mouse',cv2.WINDOW_AUTOSIZE)
cv2.resizeWindow('mouse',640,360)

#设置鼠标回调
cv2.setMouseCallback('mouse',mouse_callback,'123')

#显示窗口和背景
img = np.zeros((360,640,3),np.uint8)
while True:
    cv2.imshow('mouse',img)
    key = cv2.waitKey(100)
    if key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()