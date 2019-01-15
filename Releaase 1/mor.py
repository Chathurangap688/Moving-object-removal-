from PIL import Image
import numpy as np
import os
from scipy import misc
class MovingObjectRemover:

    def __init__(self):
        print("ObjectCreated")

    def load_image( self,infilename ) :
        img = Image.open( infilename )
        img.load()
        data = np.asarray( img, dtype="int32" )
        return data

    def save_image( self,npdata, outfilename) :
        misc.imsave(outfilename, npdata)
        
    def open_image_set(self,file_path):
        files = os.listdir(file_path)
        images=[]
        for image in files:
            images.append(self.load_image(file_path+'/'+image))
        return images
        
    def compute_and_save(self,img,path='./tmp.jpg'):
        self.save_image(np.median(img,axis=0),path)
