#导入模块
import cv2 as cv
#检测函数
def face_detect_demo():
    gary= cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 颜色可以更改
    face_detect = cv.CascadeClassifier(
        "/Users/zhao/Desktop/opencv-opencv-53296de/data/haarcascades/haarcascade_frontalface_alt2.xml")

    #face_detect = cv.CascadeClassifier("/Users/zhao/Downloads/opencv-opencv-53296de/data/haarcascades_cuda/haarcascade_frontalface_default.xml")
    #face=face_detect.detectMultiScale(gary,1.05,5,0,(10,10),(1200,1200))#框人脸的范围
    face = face_detect.detectMultiScale(gary)
    for x,y,w,h in face:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
    cv.imshow("result",img)
#读取图片
img=cv.imread("many.jpg")
face_detect_demo()
#等待
while True:
    if ord('q') == cv.waitKey(0): #按下键盘上的q就退出运行(要英文输入法的q)
        break
#按下按键后关闭窗口
cv.destroyAllWindows()