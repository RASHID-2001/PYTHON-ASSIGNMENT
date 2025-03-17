"""
QN:Write a Python program to convert a color image to a grayscale image.(2024 JANUARY)
"""
from images import Image
def grey(image):
	for y in range(image.getHeight()):
		for x in range(image.getWidth()):
            		(r, g, b) = image.getPixel(x, y)
            		gray = int(r * 0.299 + g * 0.587 + b * 0.114)  
            		image.setPixel(x, y, (gray, gray, gray))
	image.draw()  

f=input("ENTER THE FILENAME:")
i = Image(f) 
grey(i) 
i.save(f+"grey")
print("IMAGE SAVED SUCCESFULLY")


