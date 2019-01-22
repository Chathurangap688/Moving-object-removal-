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
        img=np.median(img,axis=0)
        self.save_image(img,path)
        return img
    
    #def save_image(self,img,path='./tmp.jpg'):


    def genarate_bound(self,img,x_h,x_l,y_h,y_l):
        zr_y_l=np.zeros((y_l,img.shape[1],img.shape[2]))
        zr_y_h=np.zeros((y_h,img.shape[1],img.shape[2]))
        #print ( zr[0].size)
        #print(zr.shape)
        #print(img.shape)
        resized=np.concatenate((zr_y_l,img,zr_y_h),axis=0)
        #print(resized.shape)
        #print(img.shape[1])
        zr_x_l=np.zeros((resized.shape[0],x_l,resized.shape[2]))
        zr_x_h=np.zeros((resized.shape[0],x_h,resized.shape[2]))
        resized=np.concatenate((zr_x_l,resized,zr_x_h),axis=1)
        return resized
    
    def bound_for_each(self,imgs,bound_x,bound_y):
        ret = []
        for img in imgs:
            ret.append(self.genarate_bound(img,bound_x,bound_x,bound_y,bound_y))
        return ret

    def get_best_match(self,im_base,im_second,bound=10):
        base_d=self.gradiant(im_base,5)
        base_image=self.genarate_bound(base_d,bound,bound,bound,bound)[bound:-1*bound,bound:-1*bound]
        
        img_d =self.gradiant(im_second,5)

        best_match=[]
        score=-1
        pos=[0,0]
        
        
        for x in range(bound*2-1):
            for y in range(bound*2-1):
                tmp = self.genarate_bound(img_d,x,bound*2-x,y,bound*2-y)[bound:-1*bound,bound:-1*bound]
                score_tmp = np.sum(np.absolute(base_image-tmp))
                if (((score_tmp)<score) or score<0):
                    #self.save_image(np.absolute((base_image-tmp)),'./best_match.jpg')
                    score=score_tmp
                    pos=[x,y]
                    best_match=self.genarate_bound(im_second,x,bound*2-x,y,bound*2-y)

        print('Calculated best shift is:'),
        print(pos)
        return best_match[bound:-1*bound,bound:-1*bound]
    
    def gradiant(self,img,order):
        im1=self.genarate_bound(img,0,order,0,0)
        im2=self.genarate_bound(img,order,0,0,0)
        dif = np.absolute(im1-im2)
        return dif
    
    def get_stabilized_imageset(self,imgs,order):
        ret_imgs=[]
        for img in imgs:
            ret_imgs.append(self.get_best_match(imgs[0],img,order))
        return ret_imgs

App = MovingObjectRemover()
images= App.open_image_set("../pond")
stab_images=App.get_stabilized_imageset(images,5)
App.compute_and_save(stab_images,'./Stabilized_output.jpg')

