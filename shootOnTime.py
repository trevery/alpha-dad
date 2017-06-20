from SimpleCV import Camera, Image
import time

cam = Camera()
numFrames = 10

for x in range(0, numFrames):
    img = cam.getImage()
    filepath = "image-" + str(x) + ".jpg"
    img.save(filepath)
    print "Saved image to: " + filepath
    time.sleep(60)

