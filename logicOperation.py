import picOperation

import os
import cv2
import numpy

def saveRoiImg(origImgPath, roiImgPath, leftUpLoc, leftDownLoc, rightUpLoc, rightDownLoc):
    '''
    func: obtain the roi of the original figure, save
    para: filePath = "C:/Users/mi/Desktop/Untitled Folder"
          fileName = "checkImg1.bmp"
          leftUpLoc, leftDownLoc, rightUpLoc, rightDownLoc = location of the roi
    return: none, save the roi image
    '''
    for origImgName in os.listdir(origImgPath):
        if origImgName.endswith('.bmp'):  # 代表结尾是bmp格式的
            origImg = cv2.imread(origImgPath + '/' + origImgName, cv2.IMREAD_GRAYSCALE)
            roiImg = origImg[leftUpLoc:leftDownLoc, rightUpLoc:rightDownLoc]
            cv2.imwrite(roiImgPath + '/' + origImgName, roiImg)
            picOperation.cvShow(roiImg)
#     origImg = cv2.imread(filePath+'/'+ fileName,cv2.IMREAD_GRAYSCALE)
#     roiImg = origImg[leftUpLoc:leftDownLoc,rightUpLoc:rightDownLoc]
#     cv2.imwrite(filePath+'/'+ "roi_"+fileName, roiImg)
#     cv2.namedWindow('check_roi_image',cv2.WINDOW_NORMAL) #cv2.WINDOW_AUTOSIZE
#     cv2.imshow("check_roi_image",roiImg)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()



def getImageRecognize_(templImgPath, origImgPath): #方案1 的模板匹配
    """ obtain all image"""
    for origImgName in os.listdir(origImgPath):
        if origImgName.endswith('.bmp'):  #代表结尾是bmp格式的
            origImg = cv2.imread(origImgPath+'/'+ origImgName,cv2.IMREAD_GRAYSCALE)
            for templImgName in os.listdir(templImgPath):
                if templImgName.endswith('.jpg'):  #代表结尾是bmp格式的
                    tempImg = cv2.imread(templImgPath+'/'+ templImgName,cv2.IMREAD_GRAYSCALE)
                    # 匹配的操作：
                    templImgMatch(tempImg, origImg)
#                     tempImg = cv2.GaussianBlur(tempImg,(5,5),0) #img1_copy1 = numpy.copy(img1_copy)
#                     tempImg = cv2.Canny(tempImg,100,200)

                    cv2.namedWindow('ImgShow',cv2.WINDOW_NORMAL)
                    cv2.imshow("ImgShow",tempImg)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()


def templImgMatch(templImg, origImg): #方案1 的辅助函数
    origImg_copy = numpy.copy(origImg)

    height, width = templImg.shape
    results = cv2.matchTemplate(origImg, templImg, cv2.TM_CCOEFF_NORMED)
    # cv2.TM_SQDIFF_NORMED 标准差值平方和的匹配方式
    # cv2.TM_CCOEFF_NORMED 按照标准相关系数匹配

    for y in range(len(results)):
        for x in range(len(results[y])):
            if results[y][x] > 0.7:
                cv2.rectangle(origImg_copy, (x, y), (x + width, y + height), (0, 0, 255), 2)

    #     minValue, maxValue, minLoc, maxLoc = cv2.minMaxLoc(results)# 获取匹配结果中的最小值、最大值、最小值坐标和最大值坐标
    #     resultPoint1 = minLoc
    #     resultPoint2 = (resultPoint1[0] + width, resultPoint1[1] + height)

    #     cv2.rectangle(origImg_copy, resultPoint1, resultPoint2, (0, 0, 255), 2) ######
    cv2.namedWindow('obtainTarget', cv2.WINDOW_NORMAL)
    cv2.imshow("obtainTarget", origImg_copy)  ####
    cv2.waitKey()
    cv2.destroyAllWindows()


# def getSplitLetter(origImg, x, y, w, h):
#     letterImg = origImg[x:x+w, y:y+h]
#     return letterImg

