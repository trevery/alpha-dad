#! /usr/bin/env python

'''
To: Take some photos at random time from the system up.
Author: Can
Time:20,Jun,2017

'''
import os

#timelapse
##for example: raspistill -o frame%04d.jpg -tl 10000 -t 60000

timelapse = '2000'
timeout   = '20000'
os.system("raspistill -o ~/alpha-dad/photos/takeSomePhotos/frame%03d.jpg -tl "+timelapse+" -t "+timeout)

