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
		inverted_img_pixels = np.ndarray(shape=(img.size[0], img.size[1]), dtype=float)
		for y in range(0, img.size[0]):
			for x in range(0, img.size[1]):
				pixel = img.getpixel((x, y))
				inverted_img_pixels[y][x] = 0 if pixel == (0,0,0) else 1
		plt.imsave('data/JOSM/train/label/' + image_path, inverted_img_pixels, cmap=cm.gray)

cropImages = cropImages()
preprocessImage = preprocessImage()
preprocessLayer = preprocessLayer()