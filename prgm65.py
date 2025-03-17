"""
QN:Write a python program to convert a colour image to black and white image.
Explain the image methods used in it.(MAY 2023)

"""
from images import Image
def bal_w(image):
	blackpixel=(0,0,0)
	whitepixel=(255,255,255)
	for y in range(image.getHeight()):
		for x in range(image.getWidth()):
			(r,g,b)=image.getPixel(x,y)
			avg=(r+g+b)/3
			if avg<128:
				image.setPixel(x,y,blackpixel)
			else:
				image.setPixel(x,y,whitepixel)

f=input("ENTER THE FILENAME:")
i=Image(f)
i.draw()
bal_w(i)
i.draw()
i.save(f+"b&w")
print("IMAGE SAVED SUCCESFULLY")