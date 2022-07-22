import cv2
import numpy
import logicOperation

def cvShow(origImg):
    cv2.namedWindow(' ',cv2.WINDOW_NORMAL) #WINDOW_AUTOSIZE
    cv2.imshow(" ",origImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

def getCanny(origImg, blurNumber=5):
    '''边缘检测'''
    cannyImg = cv2.bitwise_not(origImg)
    # cannyImg = cv2.GaussianBlur(origImg, (blurNumber, blurNumber), 0)  # img1_copy1 = numpy.copy(img1_copy)
    # cannyImg = cv2.Canny(origImg, 100, 200)  # 100,200
    # cvShow(cannyImg)
    cannyImg = getDilate(cannyImg, 5)
    cannyImg = getDilate(cannyImg, 5)
    cannyImg = getDilate(cannyImg, 5)
    # # cannyImg = getErosion(cannyImg)
    # cvShow(cannyImg)


    contours, hierarchy = cv2.findContours(cannyImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # cv2.RETR_TREE
    #     cannyImg = cv2.drawContours(cannyImg, contours, -1, (100,100,100), 2)
    i=1
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if w>25 and h>45 and w<90 and h<90 and i<=20:
            print(w,h)
            cv2.rectangle(origImg, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # letterImg = origImg[x:x+w, y:y+h] # 分割字符成图片
            # cv2.imwrite('./pictures/origImg.jpg', letterImg)

            print(i)
            i += 1
        # cv2.rectangle(origImg, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # cv2.imwrite('./pictures/origImg222.jpg', origImg)


    cvShow(origImg) ###################
    # cv2.imwrite('./pictures/origImg.jpg', origImg)
    return #cannyImg


def getDilate(origImg, iterNum = 2):
    '''膨胀操作'''
    # iterNum  迭代次数，也就是执行几次膨胀操作
    kernel = numpy.ones((3, 3), dtype=numpy.uint8)  # 卷积核为3*3
    dilateImg = cv2.dilate(origImg, kernel, iterNum)
    return dilateImg


def getErosion(origImg, iterNum = 2):
    '''腐蚀操作'''
    #iterNum 迭代次数
    kernel = numpy.ones((3, 3), dtype=numpy.uint8)
    erosionImg = cv2.erode(origImg, kernel, iterations=iterNum)
    #     erosionImg = numpy.hstack((origImg, erosion))
    return erosionImg

# def getMorphology(origImg, iterNum = 2):
#     '''形态学开运算，先腐蚀再膨胀，消除噪点'''
#     # origImg 二值化后的灰度图
#     # iterNum 迭代次数
#     kernel = numpy.ones((3, 3), dtype=numpy.uint8)
#     openingImg = cv2.morphologyEx(origImg, cv2.MORPH_OPEN, kernel, iterations=iterNum)
#     return openingImg

def watershedAlgoImgSeg(origImg):
    '''分水岭算法实现图像分割'''
    # origImg RGB图
    origImgCopy = cv2.cvtColor(origImg, cv2.COLOR_BGR2GRAY) #转灰度图
    thresh = cv2.adaptiveThreshold(origImgCopy, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 10) #7,6 #11,10 #邻域块大小选择 | 偏移值调整量，用均值和高斯计算阈值后，再减或加这个值就是最终阈值

    # ret, thresh = cv2.threshold(origImgCopy, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU) #将灰度图阈值化，分成黑白两个部分  #cv2.THRESH_OTSU 适合双峰值图像，我们的图像是单峰值的
    # print("ret of thresh:", ret)
    cvShow(thresh) #输出给神经网络，后面的处理用于定位
    # cv2.imwrite('./pictures/thresh0.jpg', thresh)
    # cannyImg = getCanny(thresh)
    # cvShow(cannyImg)
    # cv2.imwrite('./pictures/cannyImg.jpg', cannyImg)


    kernel = numpy.ones((3, 3), dtype=numpy.uint8)
    openingImg = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=4) #形态学开运算，先腐蚀再膨胀，消除噪点
    # cvShow(openingImg)
    getCanny(openingImg)
    # cv2.imwrite('./pictures/openingImg.jpg', openingImg)
    # sureBG = cv2.dilate(openingImg, kernel, iterations=3) #获得确定的背景区域
    # cvShow(sureBG)
    # distTransform = cv2.distanceTransform(openingImg, cv2.DIST_L2, 5)
    # ret, sureFG = cv2.threshold(distTransform, 0.7*distTransform.max(), 255, 0)
    # sureFG = sureFG.astype(numpy.uint8) #获得确定的前景区域
    # cvShow(sureFG)
    # unknowG = cv2.subtract(sureBG, sureFG) #获得未知区域，即非前景和背景
    # cvShow(unknowG)
    # ret, markers = cv2.connectedComponents(sureFG) #构建屏障
    # markers += 1
    # markers[unknowG==255] = 0 #保持未知区域为0
    # markers = cv2.watershed(origImg, markers)
    # origImg[markers==-1] = [255,0,0]
    # cvShow(origImg)
    # cv2.imwrite('./pictures/origImg.jpg', origImg)
    return