from directories import *

import numpy as np
import os
import cv2
from tqdm import tqdm
import random
import xml.etree.ElementTree as ET
import pandas as pd

IMG_SIZE = 100
training_data = []
test_data = []


def get_class_from_annotation(img_name,category):
    class_categories = []
    categories = ["train_val","test"]
    if category == categories[0]:
        ann_path = TRAIN_IMAGES_ANNOTATIONS
    else:
        ann_path = TEST_IMAGES_ANNOTATIONS

    try:
        tree = ET.parse(r"{ann}\{img}.xml".format(ann=ann_path, img=img_name))
        root = tree.getroot()

        for object in root.findall('object'):
            name = object.find('name').text
            class_categories.append(name)
    
    except Exception as e:
        print(f"Error parsing XML of object for image {img_name}: {e}")
        return []  # Return an empty list in case of errors
    
    return class_categories

def get_bbox_coordinates(img_name, category):
    coordinates = []
    categories = ["train_val","test"]
    if category == categories[0]:
        ann_path = TRAIN_IMAGES_ANNOTATIONS
    else:
        ann_path = TEST_IMAGES_ANNOTATIONS

    try:
        tree = ET.parse(r"{ann}\{img}.xml".format(ann=ann_path, img=img_name))
        root = tree.getroot()
        coordinates = []

        for object in root.findall('object'):
            bbox = object.find('bndbox')
            xmin = int(bbox.find('xmin').text)
            ymin = int(bbox.find('ymin').text)
            xmax = int(bbox.find('xmax').text)
            ymax = int(bbox.find('ymax').text)
            coordinates.append([xmin, ymin, xmax, ymax])

        return coordinates 
    except Exception as e:
        print(f"Error parsing XML of bbox for image bbox {img_name}: {e}")
        return []  # Return an empty list in case of errors

def create_train_val_dataset():
    # Define the path to the dataset
    img_path = TRAIN_IMAGES
    for img in tqdm(os.listdir(img_path)):
        try:
            img_array = cv2.imread(os.path.join(img_path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
            new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize to normalize data size
            training_data.append([new_array, get_class_from_annotation(str(img[:-4]), "train_val"), get_bbox_coordinates(str(img[:-4]), "train_val")])  # add this to our training_data
        except Exception as e:  # in the interest in keeping the output clean...
            pass
    random.shuffle(training_data)

    x_train = []
    y_train = []
    bndbox_coordinates = []

    for imgs_array, labels, bboxs in training_data:
        x_train.append(imgs_array)
        y_train.append(labels)
        bndbox_coordinates.append(bboxs)

    x_train = np.array(x_train).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    y_train = np.array(y_train)
    bndbox_coordinates = np.array(bndbox_coordinates)

    return x_train, y_train, bndbox_coordinates


def create_test_dataset():
    # Define the path to the dataset
    img_path = TEST_IMAGES

create_train_val_dataset()
training_data = pd.DataFrame(training_data)

print(training_data.shape)