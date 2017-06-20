#! /usr/bin/env python

'''
To: get photos from '../photos/takeSomePhotos/'
Author: trevery
Time: 20, Jun, 2017
'''

import os
imgDir = '../photos/takeSomePhotos/'

def getImageCount(imgDir):
	imgList = os.listdir(imgDir)
	imgCount = len(imgList)
	return imgCount

def getImageList(imgDir):
	imgList = os.listdir(imgDir)
	return imgList
	
def getAbsDir(imgName):
	imgAbsDir = '~/alpha-dad/photos/takeSomePhotos/'+imgName
	return imgAbsDir	
	
imgList = getImageList(imgDir)
#print imgList
imgCount = getImageCount(imgDir)
#print imgCount
for i in range(0,imgCount):
	imgAbsDir = getAbsDir(imgList[i])
	print('image:'+imgAbsDir)
	os.system('dream -i'+'imgAbsDir')
	



