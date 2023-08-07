import cv2
#video capture ()
#read(状态值ture，视频帧)
#创建窗口
cv2.namedWindow('video',cv2.WINDOW_AUTOSIZE)

#获取视频设备 命名为cap####  从视频读取视频帧 参数加上(视频地址)
cap = cv2.VideoCapture("D:\Download\lallla.mp4")

while True:
        #ret 是否真的读到视频帧了 frame 视频帧
        ret, frame  = cap.read()
#将视频帧在窗口中显示
        cv2.imshow('video',frame)
#等待键盘事件，q退出
        key = cv2.waitKey(5)  #播放视频大概参数设置  数字=1000/帧数
        if(key & 0xFF == ord('q')):
            break

#释放videocapture
cap.release()
cv2.destroyAllWindows()