#! /usr/bin/env python

import os
import time

currentTime = time.strftime(r"%Y-%m-%d_%H-%M-%S",time.localtime())
imgDir = '/home/pi/alpha-dad/photos/'
os.chdir(imgDir)
# if (file.jpg):
os.system('avconv -r 0.5 -i frame%03d.jpg -r 0.5 -vcodec libx264 ../video/timelapse'+currentTime+'.mp4')

#  delete all photos for next time
os.system('rm *')
