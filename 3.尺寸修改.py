#导入模块
import cv2 as cv
#读取图片
img=cv.imread("嘟嘟.jpg")
#修改尺寸
resize_img=cv.resize(img,dsize=(200,200))
#显示原图
cv.imshow("img",img)
#显示修改后的图
cv.imshow("resize_img",resize_img)
#打印原图大小
print("未修改",img.shape)
#打印修改后的大小
print("修改后",resize_img.shape)
#等待
while True:
    if ord('q') == cv.waitKey(0): #按下键盘上的q就退出运行(要英文输入法的q)
        break
#按下按键后关闭窗口
cv.destroyAllWindows()