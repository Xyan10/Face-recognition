#导入模块
import cv2 as cv
#摄像头
cap=cv.VideoCapture(0)

flag=1
num=1

while (cap.isOpened()):#检测摄像头是否打开
    ret_flag,Vshwo=cap.read()#得到每帧图像
    cv.imshow("Capture_test",Vshwo)
    k=cv.waitKey(1)&0xFF#按键判断
    if k==ord('s'):#保存
        cv.imwrite("/Users/zhao/Desktop/录入/"+str(num)+'.name'+'.jpg',Vshwo)
        print('success to save'+str(num)+'.jpg')
        print('___________')
        num+=1
    elif k==ord(" "):#退出
        break

#释放摄像头
cap.release()
#释放内存
cv.destroyAllWindows()
