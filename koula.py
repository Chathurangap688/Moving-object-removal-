from PIL import Image
import numpy as np
import os
from scipy import misc
def load_image( infilename ) :
    img = Image.open( infilename )
    img.load()
    data = np.asarray( img, dtype="int32" )
    return data

def save_image( npdata, outfilename) :
    misc.imsave(outfilename, npdata)

    
def open_image_set(file_path):
    files = os.listdir(file_path)
    images=[]
    for image in files:
        images.append(load_image(file_path+'/'+image))
    return images
    
#-----------------------------------------------------
img=open_image_set('./ams')
print(type(np.asarray(img[0])))
im = Image.open('./ams/0.jpg')
save_image(np.median(img,axis=0),'./output3.jpg')