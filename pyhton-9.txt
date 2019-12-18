# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 02:38:38 2019

@author: AHMAD
"""

"""  Ques 1  """





import math
import statistics as st
import random

X = [ 3 , 1.5 , 4.5 , 6.75 , 2.25 , 5.75 , 2.25 ]

print(st.mean(X))

print(st.harmonic_mean(X))

print(st.median(X))

print(st.median_low(X))

print(st.median_high(X))

print(st.median_grouped(X))

print(st.mode(X))

print(st.pstdev(X))  

print(st.pvariance(X))  
     
print(st.stdev(X))

print(st.variance(X))  
  




     

"""  Ques 2  """



print(random.random())

print(random.randrange(10))

print(random.choice([ 'Ali', 'Khalid' , 'Hussam' ]) )


print( random.sample(range(1000), 10) )

print(random.choice('Orange Academy') )

print(random.shuffle(X) )

print(random.randint(20, 30) )

print(random.randrange(1000,2111,5))

print(random.uniform(10000,11000))




"""  Ques 3  """

print(math.pi)

print(math.cos(200))

print(math.sin(30))

print(math.tan(180))

print(math.floor(10.8))

print(math.ceil(10.8))


"""  Ques 4  """

"""   A   """
from PIL import Image
im=Image.open("download.jpg")
print(im.format,im.size,im.mode)
im.show()




"""   B   """
from PIL import Image
im=Image.open("download.jpg")
rotated=im.rotate(180)
rotated.show()



"""   C   """
from PIL import Image
image = Image.open("download.jpg")
greyscale_image = image.convert('L')
greyscale_image.show()




"""   D   """

from PIL import Image
original = Image.open("download.jpg")
cropped = original.crop((0,0,50,50))
cropped.show()



"""   E   """

from PIL import Image
from PIL import ImageDraw
im = Image.open("download.jpg")
draw = ImageDraw.Draw(im)
draw.line((0,0) + im.size , fill=(255,255,255) )
draw.line((0, im.size[1] , im.size[0],0) , fill=(255,255,255) )
draw.text((im.size[0]/2 - im.size[0]/2 , im.size[1]/2 + 20 ),"Ahmad Taha", fill=(255,255,0))
im.show()



"""   F   """

from PIL import Image , ImageFilter
original = Image.open('download.png')
newimg1  = original.filter(ImageFilter.EDGE_ENHANCE)
newimg2  = original.filter(ImageFilter.FIND_EDGES)
newimg3  = original.filter(ImageFilter.SMOOTH)
newimg4  = original.filter(ImageFilter.SHARPEN)


newimg1.show()
newimg2.show()
newimg3.show()
newimg4.show()




"""   G   """




from PIL import Image
alpha = 0.5

img1 = Image.open("cat.png")
img2 = Image.open("dog.png").resize(img1.size)
Image.blend(img1,img2,alpha).save("New.png".format(alpha))
im = Image.open("New.png")
im.show()


"""   H   """

from PIL import Image , ImageFilter
original = Image.open("download.jpg")
blurred=original.filter(ImageFilter.BLUR)
original.show()
blurred.show()





"""   I   """

from PIL import Image

size = (128,128)
saved = "download.jpg"


try:
    im = Image.open("download.jpg")

except:
    print("Unable to load image")

im.thumbnail(size)
im.save(saved)
im.show()




"""   J   """


from PIL import Image
im=Image.open("download.jpg")
rotated=im.rotate(90)
rotated.show()


"""   K   """

from PIL import Image
img1 = Image.open('A')
img2 = Image.open('B').resize(img1.size)
mask = Image.open('mask')
mask = mask.resize(img1.size)
Image.composite(img1,img2.mask).save("Image_composite.jpg")
im = Image.open("Image_composite.jpg")
im.show()

