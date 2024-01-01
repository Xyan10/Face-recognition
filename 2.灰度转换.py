#导入模块
import cv2 as cv
#读取图片
img=cv.imread("嘟嘟.jpg")
#灰度转换
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)#颜色可以更改
#显示灰度
cv.imshow("gray",gray_img)
#保存灰度图片
cv.imwrite("grayface.jpg",gray_img)
#显示图片
cv.imshow('read_img',img)
#设置停止按键
cv.waitKey( )
#按下按键后关闭窗口
cv.destroyAllWindows()