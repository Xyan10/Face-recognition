#导入模块
import cv2 as cv
#读取图片
img=cv.imread("嘟嘟.jpg")
#显示图片
cv.imshow('read_img',img)
#设置停止按键
cv.waitKey( )
#按下按键后关闭窗口
cv.destroyAllWindows()