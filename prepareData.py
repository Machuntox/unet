# greyscale img
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import PIL.ImageOps
import os

def cropImages():
	imageFolder = 'data/JOSM/train/imgRaw'
	labelFolder = 'data/JOSM/train/labelRaw'

	for counter in range(1508):
		image = Image.open(imageFolder + '/image' + str(counter) + '.png')
		croppedImage = image.crop((0, 0, 512, 512))
		croppedImage.save('data/JOSM/train/imageCropped/' + str(counter) + '.png')

		label = Image.open(labelFolder + '/layer' + str(counter) + '.png')
		croppedLabel = label.crop((0, 0, 512, 512))
		croppedImage.save('data/JOSM/train/labelCropped/' + str(counter) + '.png')

def preprocessImage():
	folder = 'data/JOSM/train/imageCropped'

	for image_name in os.listdir(folder):
		img = Image.open(folder + '/' + image_name).convert('L')
		img.save('data/JOSM/train/image/' + image_name)


def preprocessLayer():
	folder = 'data/JOSM/train/labelCropped'

	for image_path in os.listdir(folder):
		img = Image.open(folder + '/' + image_path)
		img = img.convert("RGBA")
		pixdata = img.load()

		for y in range(img.size[1]):
			for x in range(img.size[0]):
				if pixdata[x, y] == (0, 0, 0, 255):
					pixdata[x, y] = (0, 0, 0, 255)
				else:
					pixdata[x, y] = (255, 255, 255, 255)
		img.save('data/JOSM/train/label/' + image_path,'PNG')

cropImages = cropImages()
preprocessImage = preprocessImage()
preprocessLayer = preprocessLayer()
