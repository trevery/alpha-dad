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
timeout   = '2000'
# the raw photos named origianFrame000.jpg and after dream, all the photos name frame000.jpg
os.system("raspistill -o ~/alpha-dad/photos/originFrame%03d.jpg -w 500 -h 280 -tl "+timelapse+" -t "+timeout)

