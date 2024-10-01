from directories import *

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
    elif category == categories[1]:
        ann_path = TEST_IMAGES_ANNOTATIONS
    else:
        print("Wrong category")

    try:
        tree = ET.parse(r"{ann}\{img}.xml".format(ann=ann_path, img=img_name))
        root = tree.getroot()

        for object in root.findall('object'):
            name = object.find('name').text
            class_categories.append(name)
    
    except Exception as e:
        print(f"Error parsing XML of object for image {img_name}: {e}")
        class_categories.append('')  # Return an empty list in case of errors
    
    return class_categories

def get_bbox_coordinates(img_name, category):
    coordinates = []
    categories = ["train_val","test"]
    if category == categories[0]:
        ann_path = TRAIN_IMAGES_ANNOTATIONS
    elif category == categories[1]:
        ann_path = TEST_IMAGES_ANNOTATIONS
    else:
        print("Wrong category")

    try:
        tree = ET.parse(r"{ann}\{img}.xml".format(ann=ann_path, img=img_name))
        root = tree.getroot()
        coordinates = []

        for object in root.findall('object'):
            bbox = object.find('bndbox')
            xmin = int(round(float(bbox.find('xmin').text),0))
            ymin = int(round(float(bbox.find('ymin').text),0))
            xmax = int(round(float(bbox.find('xmax').text),0))
            ymax = int(round(float(bbox.find('ymax').text),0))
            coordinates.append([xmin, ymin, xmax, ymax])

        return coordinates 
    except Exception as e:
        print(f"Error parsing XML of bbox for image bbox {img_name}: {e}")
        coordinates.append([])
        return coordinates  # Return an empty list in case of errors

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
    return pd.DataFrame(training_data)


def create_test_dataset():
    # Define the path to the dataset
    img_path = TEST_IMAGES
    for img in tqdm(os.listdir(img_path)):
        try:
            img_array = cv2.imread(os.path.join(img_path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
            new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize to normalize data size
            test_data.append([new_array, get_class_from_annotation(str(img[:-4]), "test"), get_bbox_coordinates(str(img[:-4]), "test")])  # add this to our training_data
        except Exception as e:  # in the interest in keeping the output clean...
            pass
    random.shuffle(test_data)
    return pd.DataFrame(test_data)
