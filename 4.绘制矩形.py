#导入模块
import cv2 as cv
#读取图片
img=cv.imread("嘟嘟.jpg")
#坐标
x,y,w,h=100,100,100,100
#绘制矩形
cv.rectangle(img,(x,y,x+w,y+h),color=(0,0,255),thickness=1)
#绘制圆形
cv.circle(img,center=(x+w,y+h),radius=100,color=(255,0,0),thickness=2)
#显示
cv.imshow("re_img",img)
#等待
while True:
    if ord('q') == cv.waitKey(0): #按下键盘上的q就退出运行(要英文输入法的q)
        break
#按下按键后关闭窗口
cv.destroyAllWindows()