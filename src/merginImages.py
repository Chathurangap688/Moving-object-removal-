from __future__ import division   # for python-2.x compatibility
import imread as imread
from PIL import Image
from collections import Counter
import numpy as np
import cv2
import os

def processingImages(img_data):
    print("Processing......................")

    imaffF = [] 
    w,h= img_data[0].size
    im_sum = np.zeros((h,w,3))
    im_sum = im_sum.astype('float')
    # print im_sum
    #length of the images containing the folder
    n = len(img_data)               

    for i in range(n):
        im = np.asarray(img_data[i])
        #converting images into type float
        im = im.astype('float')
        im_sum = np.add(im_sum,im)
        # print im_sum
        #create new list with float images
        imaffF.append(im)
        # print imaffF[i]
        # print np.sum(imaffF[i])

    # print im_sum

    # trying to add each images together
    # for k in range(0,n-1,2):
    #     image = cv2.add(imaffF[k],imaffF[k+1])
        
    #trying to devide each pixel values with total number of images (to get the mean values of each pixel)
    image2 = [[item/n for item in subl] for subl in im_sum]

    #convert back to type unit8
    image = np.array(image2, dtype=np.uint8)
    resultImage = Image.fromarray(image)
    
    resultImage.save('check.jpg')

    resultImage.show()
    print("process complete..!")





def openImageFiles():
    files = []
    dir_name = './'
    dir_name += raw_input("enter input-folder name : ")
    for file in os.listdir(dir_name):
        files.append(file)

    img_data = []
    for file_name in files:
        file = dir_name+'/'+file_name
        img_data.append(imread.open_image(file))

    # im = Image.open(file)
    # output = Image.new(im.mode, im.size)
    # output_data = output.load()
    # print im
    processingImages(img_data)




if __name__ == '__main__':
    openImageFiles()