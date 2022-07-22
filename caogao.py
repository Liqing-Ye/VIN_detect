# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# import logicOperation
# import picOperation
#
# import numpy
# import os
# import cv2


# origImgPath = "C:/Users/mi/Desktop/Untitled Folder/originalImage_dataset"
# roiImgPath = "C:/Users/mi/Desktop/Untitled Folder/roiImage_dataset"
# templImgPath = "C:/Users/mi/Desktop/Untitled Folder/templeImage_dataset_v2"

# saveRoiImg(origImgPath, roiImgPath, leftUpLoc = 950, leftDownLoc = 1200, rightUpLoc = 1000, rightDownLoc = 2150)
# getImageRecognize_(templImgPath = templImgPath, origImgPath = roiImgPath) #

# origImg = cv2.imread('./roiImage_dataset/checkImg2.jpg',cv2.IMREAD_GRAYSCALE)
# print(origImg.shape)
# print(origImg.dtype) #img.dtype在调试时非常重要，因为OpenCV-Python代码中的大量错误是由无效的数据类型引起的


# cannyImg = picOperation.getCanny(origImg, blurNumber = 1)
# cv2.namedWindow('checkImg1',cv2.WINDOW_NORMAL) #WINDOW_AUTOSIZE
# cv2.imshow("checkImg1",origImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cannyImg = getDilate(cannyImg)
# cannyImg = getErosion(cannyImg)

# cv2.imwrite('save2.jpg', cannyImg)

# if __name__ == '__main__':
#     print_hi('PyCharm')

# import tesserocr
# # print(tesserocr.file_to_text("save2.jpg"))
#
# cannyImg = getDilate(cv2.imread('save2.jpg',cv2.IMREAD_GRAYSCALE), 1)
# cannyImg = getDilate(cannyImg, 1)
# cv2.imwrite('save3.jpg', cannyImg)
# print(tesserocr.file_to_text("save3.jpg"))
# print(tesserocr.file_to_text("1.png"))




# import cv2
# import numpy

# origImg1 = cv2.imread('checkImg1.bmp',cv2.IMREAD_GRAYSCALE)
# print(origImg1.shape)
# print(origImg1.dtype)
# # cv2.namedWindow('checkImg1',cv2.WINDOW_NORMAL) #WINDOW_AUTOSIZE
# # cv2.imshow("checkImg1",img1)

# img1_copy = img1[950:1200,1000:2100]
# # cv2.namedWindow('copy_1',cv2.WINDOW_AUTOSIZE)
# # cv2.imshow("copy_1",img1_copy)

# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# cv2.imwrite("./saveImg1.bmp", img1_copy)
# # cv2.imwrite("./saveImg2.jpg", img1_copy)