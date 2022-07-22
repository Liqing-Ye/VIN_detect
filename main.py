# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import logicOperation
import picOperation

import numpy
import os
import cv2
import tesserocr
from matplotlib import pyplot as plt

origImgPath = "./pictures/originalImage_dataset" #D:\Hza\pythonCode20220721\pictures\originalImage_dataset
roiImgPath = "./pictures/roiImage_dataset"
templImgPath = "./pictures/templeImage_dataset_v1"

# leftUpLoc = 950, leftDownLoc = 1200, rightUpLoc = 1000, rightDownLoc = 2150 #灰色的底的照片
# leftUpLoc = 1450, leftDownLoc = 1600, rightUpLoc = 1050, rightDownLoc = 2200 #黑色一束灯光的照片
# leftUpLoc = 1300, leftDownLoc = 1750, rightUpLoc = 1050, rightDownLoc = 2200 #黑色一束灯光的照片 最终版本
logicOperation.saveRoiImg(origImgPath, roiImgPath, leftUpLoc = 550, leftDownLoc = 640, rightUpLoc = 450, rightDownLoc = 1050)
# logicOperation.getImageRecognize_(templImgPath = templImgPath, origImgPath = roiImgPath) # 方案1的模板匹配，走不通

origImg = cv2.imread(roiImgPath+'/'+'checkImg2.jpg') # 灰度图 ,cv2.IMREAD_GRAYSCALE
# cannyImg = picOperation.getCanny(origImg, blurNumber = 1)
picOperation.watershedAlgoImgSeg(origImg)

for roiImgName in os.listdir(roiImgPath):
    if roiImgName.endswith('.bmp'):  # 代表结尾是bmp格式的
        roiImg = cv2.imread(roiImgPath + '/' + roiImgName)
        picOperation.watershedAlgoImgSeg(roiImg)


# origImg = cv2.cvtColor(origImg, cv2.COLOR_BGR2GRAY) #转灰度图
# plt.hist(origImg.ravel(), 256, [0, 256]) #image.ravel()#ravel函数功能是将多维数组降为一维数组,统计各个bin的频次，256：bin的个数，[0, 256]：范围
# plt.show() #和OpenCV中的想要的直方图不同


# if __name__ == '__main__':
#     print_hi('PyCharm')


# print(tesserocr.file_to_text("save3.jpg"))##################
print("begin---")
# print(tesserocr.file_to_text("./pictures/thresh0.jpg"))############
print("end---")


