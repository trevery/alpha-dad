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

## convert face-photos into a video with "avcon"

