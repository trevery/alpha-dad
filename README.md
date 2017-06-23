# alpha-dad
let alpha 1 dream a dream

## take some photos with `raspstill`

example： 

`raspistill -o frame%04d.jpg -tl 10000 -t 60000`

This will take one photo per 10 s and will last for 60 s
Photos will be saved as frame0000.jpg frame0001.jpg.

## pick up these photos with face using `SimpleCV`

`frame.findHaarFeatures('face')` will return a list
contain faces' x,y coordinates.

and i wrote a python script named faceFilter.py to find if there are face in the photo. 


## deep dream

`pi@alpha_pi3:~/deepdream/PsyCam $ python psycam.py -i imgDir.jpg`

I have wrote an alias for this python command. 
`alias dream='python ~/deepdream/PsyCam/psycam.py`

While, I found only in the directory '~/deepdream/PsyCam', 
this command can execute rightly. In other words, 
if you in ~ directory, it will throw fault.



## convert face-photos into a video with "avconv"

### install

`sudo apt-get install libav-tools`

### example:
`avconv -r 10 -i frame%03d.jpg -r 10 -vcodec libx264 timelapse.mp4`

### new line

