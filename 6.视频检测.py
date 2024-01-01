#导入模块
import cv2 as cv
#检测函数
def face_detect_demo(img):
    gary= cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 颜色可以更改
    face_detect=cv.CascadeClassifier("/Users/zhao/Desktop/opencv-opencv-53296de/data/haarcascades/haarcascade_frontalface_alt2.xml")
    #face=face_detect.detectMultiScale(gary,1.05,5,0,(10,10),(1200,1200))#框人脸的范围
    face = face_detect.detectMultiScale(gary)
    for x,y,w,h in face:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
    cv.imshow("result",img)

#读取摄像头
#cap=cv.VideoCapture(0)#括号里是0用的是电脑自带的默认摄像头
cap=cv.VideoCapture('zxy.mp4')

#循环
while True:      #按下除q外的其他键摄像头会截取下一张图片并进行人脸识别
    flag,frame=cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord('q') == cv.waitKey(0): #按下键盘上的q就退出运行(要英文输入法的q)
        break
#按下按键后关闭窗口
cv.destroyAllWindows()
#释放摄像头
cap.release()