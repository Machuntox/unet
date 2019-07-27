from PIL import Image
import os

labelFolder = 'labels'
imageFolder = 'images'

imagesNumber = 27
labelsNumber = 27

for image_name in os.listdir(imageFolder):
    image_obj = Image.open(imageFolder + '/' + image_name)
    image_obj.save('images1/' + str(imagesNumber) + '.png')
    imagesNumber += 1

for image_name in os.listdir(labelFolder):
    image_obj = Image.open(labelFolder + '/' + image_name)
    image_obj.save('labels1/' + str(labelsNumber) + '.png')
    labelsNumber += 1
