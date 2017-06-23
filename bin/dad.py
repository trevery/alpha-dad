#! /usr/bin/env python

'''
To: get photos from '../photos/'
Author: trevery
Time: 20, Jun, 2017
'''

import os
import subprocess
imgDir = '/home/pi/alpha-dad/photos/'

def getImageCount(imgDir):
	imgList = os.listdir(imgDir)
	imgCount = len(imgList)
	return imgCount

def getImageList(imgDir):
	imgList = os.listdir(imgDir)
	return imgList
	
def getAbsDir(imgName):
	imgAbsDir = imgDir+imgName
	return imgAbsDir	
	
imgList = getImageList(imgDir)
#print imgList
imgCount = getImageCount(imgDir)
#print imgCount
for i in range(0,imgCount):
	imgAbsDir = getAbsDir(imgList[i])
	
	#print('image:'+imgAbsDir)
	# dream only can be use rightly in directory
	# `~/deepdream/PsyCam/`
	#os.curdir(".")
	
	os.chdir('/home/pi/deepdream/PsyCam/')
	
	#os.system('cd ~/deepdream/PsyCam/')
	#print(os.getcwd())
	#os.system('pwd')
	#subprocess.call('python psycam.py -i'+'imgAbsDir')
	
	
	##dream
	os.system('python psycam.py -i '+imgAbsDir)

##format images' name
imgList = getImageList(imgDir)
imgCount = getImageCount(imgDir)
for i in range(0,imgCount):
	imgName = imgList[i]
	print ('imgName: ' + imgName)
	#print(('mv '+imgName+' '+'frame00'+str(i)+'.jpg'))
	os.chdir('/home/pi/alpha-dad/photos/')
	#os.getcwd()
	os.system('mv '+imgName+' '+'frame'+('%03d' %i)+'.jpg')
	
	

