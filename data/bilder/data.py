from PIL import Image
import os

labelFolder = 'labels'
imageFolder = 'images'

imagesNumber = 0
labelsNumber = 0

# must be used with python2
for image_name in os.listdir(imageFolder):
    number = int(filter(str.isdigit, str(image_name)))
    image_obj = Image.open(imageFolder + '/' + image_name)
    image_obj.save('images1/' + str(number + 27) + '.png')
    imagesNumber += 1

for label_name in os.listdir(labelFolder):
    number = int(filter(str.isdigit, str(label_name)))
    image_obj = Image.open(labelFolder + '/' + label_name)
    image_obj.save('labels1/' + str(number + 27) + '.png')
    labelsNumber += 1
