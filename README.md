# alpha-dad
let alpha 1 dream a dream

## What I used in this project
 |Meterial| Quantity | Describtion
 |----|------|---|
 |Alpha 1 |  x 1||
 |Raspberry Pi 3 | x 1||
 |8G TF card | x 1||
 |Camera Module v3| x 1|
 |5v dc dc buck power supply module|x 1| |
 |Hexagonal stud| about 5| d 2.5|

## How to use this repo.
### The robot we've sent.

1. The Robot we've sent by post  can be used directly. I have installed all components and pushed this repo into local.
2. First, you must find someway to get use ssh to connecte to the pi 3 on the robot. Maybe you choose to use an enthernet cable connect pi3 with your router, anyway, find a way to connect the pi inside the robot.
    ```
    User:pi
    Passwd: alpha-dad
    ```
3. Once you connect this pi, you can use command bellow.
```
cd ~/alpha-dad/bin  
```
This is where contains python programs.
```
python takePhotos.py  
```
Take some photos with the camera module on the robot's head.
```
python dad.py  
```
This will last for a long time, and maybe you loose connection with pi, because this process needs lots of resource, so that your pi will get into a state like sleep. Be patient, you'd better have a drink.

 ```
 sudo python conVideo.py
 ```
This will convert photos into a small video, which can be found in the `alpha-dad/video` directory.

 Then you can download this video with `scp`. 

-----
### New Raspberry Pi 3 with jessie.
1. First, install Google Dream on your pi3(only). Read this [artical](http://www.knight-of-pi.org/deepdream-on-the-raspberry-pi-3-with-raspbian-jessie/)
2. Clone this repo into your home directory. Be sure your pi is connecting with internet.
```
cd ~
git clone https://github.com/trevery/alpha-dad.git
```
3.  do as above 'The robot we've sent'


------
# Below is some test commands.

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
