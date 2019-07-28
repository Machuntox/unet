# greyscale img
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import PIL.ImageOps
import os

def cropImages():
	imageFolder = 'data/JOSM/train/imageRaw'
	labelFolder = 'data/JOSM/train/labelRaw'


	for image_name in os.listdir(imageFolder):
		image_obj = Image.open(imageFolder + '/' + image_name)
		cropped_image = image_obj.crop((0, 0, 512, 512)) #(x1, y1, x2,y2)
		cropped_image.save('data/JOSM/train/imageCropped/' + image_name)
		
	for image_name in os.listdir(labelFolder):
		image_obj = Image.open(labelFolder + '/' + image_name)
		cropped_image = image_obj.crop((0, 0, 512, 512)) #(x1, y1, x2,y2)
		cropped_image.save('data/JOSM/train/labelCropped/' + image_name)

def preprocessImage():
	folder = 'data/JOSM/train/imageCropped'

	for image_name in os.listdir(folder):
		img = Image.open(folder + '/' + image_name).convert('LA')
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