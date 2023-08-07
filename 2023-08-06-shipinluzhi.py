#视频录制
#videowriter()参数一：输出文件 参数二：多媒体文件格式 参数三：帧率 参数四：分辨率
#write
#release


import cv2
#video capture ()
#read(状态值ture，视频帧)

#创建videowriter为多媒体文件
fourcc = cv2.VideoWriter_fourcc(*'mp4v')


vm = cv2.VideoWriter(r'C:\video\out2.mp4',fourcc,30,(1280,720))

#创建窗口
cv2.namedWindow('video',cv2.WINDOW_AUTOSIZE)

#获取视频设备 命名为cap
cap = cv2.VideoCapture(0)


#摄像头是否为打开状态
while cap.isOpened():
        
#ret 是否真的读到视频帧了 frame 视频帧
        ret, frame  = cap.read()
        if ret == True:
        #将视频帧在窗口中显示
                cv2.imshow('video',frame)
                cv2.resizeWindow('video',1280,720)

        #写数据到到媒体文件
                vm.write(frame)

        #等待键盘事件，q退出
                key = cv2.waitKey(1)
                if(key & 0xFF == ord('q')):
                        break
        else:
                break

#释放videocapture
cap.release()

#释放videowriter资源
vm.release()

cv2.destroyAllWindows()