#对图片进行人脸特征提取，将名字和对应特征对应存在文件里，方便后续利用
import os
import cv2 as cv
from PIL import Image
import numpy as np

def getImageAndLabels(path):
    #存储人脸数据
    facesSamples=[]
    #存储姓名数据
    ids=[]
    #存储图片信息
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    #加载分类器
    face_detector = cv.CascadeClassifier("/Users/zhao/Desktop/opencv-opencv-53296de/data/haarcascades/haarcascade_frontalface_alt2.xml")
    #遍利列表中的图片
    for imagePath in imagePaths:
        #打开图片，灰度化PIL有九种不同模式：1(黑白)，L，P，RGB，RGBA，CMYK，YCbCr，I，F
        PIL_img=Image.open(imagePath).convert('L')
        #将图像转化为数据
        img_numpy=np.array(PIL_img,'uint8')
        #获取图片人脸特征
        faces=face_detector.detectMultiScale(img_numpy)
        #获取每张图片的id和姓名
        id=int(os.path.split(imagePath)[1].split('.')[0])
        for x,y,w,h in faces:
            ids.append(id)
            facesSamples.append(img_numpy[y:y+h,x:x+w])#将一个人的名字和她的面部特征对应起来
    print('id:',id)
    print('fs:',facesSamples)
    return facesSamples,ids


if __name__ =="__main__":
    #图片路径
    path='/Users/zhao/Desktop/录入'
    #获取图像数据和id标签数据和姓名
    faces,ids=getImageAndLabels(path)
    #加载识别器
    recognizer=cv.face.LBPHFaceRecognizer_create()
    #训练
    recognizer.train(faces,np.array(ids))
    #保存文件
    recognizer.write('/Users/zhao/Desktop/trainer/trainer.yml')
