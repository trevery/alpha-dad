from SimpleCV import Image
import os

# read one image

def findFace(imgPath):
	img = Image(imgPath)
	faces = img.findHaarFeatures("face.xml")
	if faces is not None:
		#print("find faces!")
		return True
	else:
		#print("Don't find andy faces!")
		return False

#def deleteFile(imgPath):
#	os.remove(imgPath)
#	return
		
if __name__ == "__main__":
	imgPath = "../photos/test/noFace.jpg"
	face = findFace(imgPath)
	if face == True:
		print "finded faces!"
	else:
		print "No faces finded!s"
		os.remove(imgPath)

	
