#除报警系统以及找到对应的名字打在屏幕上未完成
import cv2 as cv
import os
import urllib
import urllib.request

#加载训练数据集文件
recognizer=cv.face.LBPHFaceRecognizer_create()
#加载数据
recognizer.read('/Users/zhao/Desktop/trainer/trainer.yml')
#名称
names=[]#存储的数据名字叫 图片名写的名字

#警报全局变量
#warningtime=0

#如果此人长时间在我的摄像头附近徘徊，但是我的摄像头并不认识他的话就会给手机发送报警短信
#def warning():

def face_detect_demo(img):
    gary= cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 颜色可以更改
    face_detector = cv.CascadeClassifier("/Users/zhao/Desktop/opencv-opencv-53296de/data/haarcascades/haarcascade_frontalface_alt2.xml")
    face = face_detector.detectMultiScale(gary,1.1,5,cv.CASCADE_SCALE_IMAGE,(100,100),(300,300))
    for x,y,w,h in face:#框处人脸的部分
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
        cv.circle(img, center=(x + w//2, y + h//2), radius=w//2, color=(255, 0, 0), thickness=4)
        #人脸识别
        ids,confidence=recognizer.predict(gary[y:y+h,x:x+w])#对这张人脸进行预测得到confidence值
        if confidence>80:#不可信
            #global warningtime
            #warningtime+=1
            #if warningtime>100:#说明此人脸不是我们录入的人脸
                #warning()
                #warningtime=0
            cv.putText(img,'unknown',(x+10,y-10),cv.FONT_HERSHEY_SIMPLEX,0.75,(0,255,0),1)
        else:#此人是录入的脸 confidence较小 是可信的人 要将姓名打到方框上
            cv.putText(img,'knowm',(x+10,y-10),cv.FONT_HERSHEY_SIMPLEX,0.75,(0,255,0),1)

    cv.imshow("result",img)

cap=cv.VideoCapture('much.mp4')
name=()
while True:
    flag,frame=cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord(' ')==cv.waitKey(10):#waitKey(参数)，0代表一直不退出
        break
cv.destroyAllWindows()
cap.release()