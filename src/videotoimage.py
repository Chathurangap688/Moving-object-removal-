import cv2
import os

def imageMaker(videoName):
	vidcap = cv2.VideoCapture(videoName)
	success,image = vidcap.read()
	count = 0
	imcount = 0
	success = True
	fps = vidcap.get(cv2.CAP_PROP_FPS)
	fps = int(fps)


	dirname = videoName.split(".")[0]
	# print dirname
	os.mkdir(dirname)

	while success:
	    success,image = vidcap.read()
	    if count%(fps) == 0 :
	      print('read a new frame: %d '%imcount,success)
	      cv2.imwrite(os.path.join(dirname, "frame%d.jpg" %imcount), image)
	      imcount +=1
	    count+=1

	return dirname


