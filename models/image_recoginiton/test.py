import os
from directories import *
import xml.etree.ElementTree as ET

ann = TRAIN_IMAGES_ANNOTATIONS
class_categories = []

for imgs in os.listdir(TRAIN_IMAGES):
    img = str(imgs[:-4])
    try:
        tree = ET.parse(r"{ann}\{img}.xml".format(ann=ann, img=str(img)))
        root = tree.getroot()

        for object in root.findall('object'):
            name = object.find('name').text
            class_categories.append(name)

    except Exception as e:
        print(f"Error parsing XML for image {img}: {e}")

    print(r"{ann}\{img}.xml".format(ann = ann, img = img))
    print(os.path.exists(r"{ann}\{img}.xml".format(ann = ann, img = img)))
    print(class_categories)