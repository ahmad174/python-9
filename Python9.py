# Ninth Day Exercise
import statistics as st
import random
import math
import doctest
from PIL import Image, ImageFilter, ImageDraw
print('EXERCISE 1')
x = [3, 1.5, 4.5, 6.75, 2.25, 5.75, 2.25]
mean = st.mean(x)
harmonicMean = st.harmonic_mean(x)
median = st.median(x)
medianLow = st.median_low(x)
medianHigh = st.median_high(x)
medianGrouped = st.median_grouped(x)
mode = st.mode(x)
pStdev = st.pstdev(x)
pVariance = st.pvariance(x)
stdev = st.stdev(x)
variance = st.variance(x)

print('X =', x)
print('Mean(x) =', mean)
print('Harmonic Mean(x) =', harmonicMean)
print('Median(x) =', median)
print('Median Low(x) =', medianLow)
print('Median High(x) =', medianHigh)
print('Median Grouped(x) =', medianGrouped)
print('Mode(x) =', mode)
print('Pstdev(x) =', pStdev)
print('Pvariance(x) =', pVariance)
print('Stdev(x) =', stdev)
print('Variance(x) =', variance)
#==============================================================================
print('\n\nEXERCISE 2')
randNum = random.random()
randRange = random.randrange(100)

choices = ('Ali', 'Khalid', 'Hussam')
randChoice = random.choice(choices)

randSample = random.sample(range(100), 10)
randLetter = random.choice('Orange Academy')

items = [1, 5, 8, 9, 2, 4]
shuffle = random.shuffle(items)

randInt = random.randint(20, 30)
fives = random.randrange(1000, 2111, 5)
distribution = random.uniform(10000, 11000)

print('Random Number >>>', randNum)
print('Random Range >>>', randRange)
print('CHOICES =', choices)
print('Random Choice >>>', randChoice)
print('Random Sample >>>', randSample)
print('Random Letter >>>', randLetter) 
print('BEFORE SHUFFLING >>>', items)
print('After Shuffling >>>', shuffle)
print('Random Integer >>>', randInt)
print('Steps of 5 >>>', fives)
print('Uniform Distribution >>>', distribution)
#==============================================================================
print('\n\nEXERCISE 3')
pi = math.pi
cosine200 = math.cos(math.radians(200))
sine30 = math.sin(math.radians(30))
tan180 = math.tan(math.radians(180))
floor = math.floor(10.8)
ceil = math.ceil(10.8)

print('PI =', pi)
print('COS(200) =', cosine200)
print('SIN(30) =', sine30)
print('TAN(180) =', tan180)
print('floor(10.8) =', floor)
print('ceil(10.8) =', ceil)
#==============================================================================
print('\n\nEXERCISE 4')
lemon = Image.open('lemon.jpg')
lemonFormat = lemon.format
lemonSize = lemon.size
lemonMode = lemon.mode
print('Format: ', lemonFormat)
print('Size: ', lemonSize)
print('Color mode:', lemonMode)
lemon.show()

lemonFlipped = lemon.transpose(Image.FLIP_TOP_BOTTOM)
lemonFlipped.show()

lemonGrey = lemon.convert('L')
lemonGrey.show()

lemonCropped = lemon.crop((0, 0, 50, 50))
lemonCropped.show()

mask = Image.open('mask.jpg')
draw = ImageDraw.Draw(mask)
draw.line((0, 0) + mask.size, fill = (0, 0, 0))
draw.line((0, mask.size[1], mask.size[0], 0), fill = (0, 0, 0))
draw.text((40, mask.size[1] - 25), 'Ahmad Al Ghzawi', fill = (0, 0, 0))
mask.thumbnail((750, 750))
mask.show()

lemonEdge = lemon.filter(ImageFilter.EDGE_ENHANCE)
lemonEdges = lemon.filter(ImageFilter.FIND_EDGES)
lemonSmooth = lemon.filter(ImageFilter.SMOOTH)
lemonSharpen = lemon.filter(ImageFilter.SHARPEN)
lemonEdge.show()
lemonEdges.show()
lemonSmooth.show()
lemonSharpen.show()

alpha = 0.5
mask = mask.resize(lemon.size)
blended = Image.blend(lemon, mask, alpha)
blended.show()

lemonBlur = lemon.filter(ImageFilter.BLUR)
lemonBlur.show()

lemon.thumbnail((250, 250))
lemon.show()

orange = Image.open('orange.jpg')
orangeRotate = orange.rotate(90)
orangeRotate.show()

black = Image.open('black.jpg').resize(mask.size)
orange = orange.resize(mask.size)
composite = Image.composite(mask, orange, black)
composite.show()

orange.save('orange.bmp')