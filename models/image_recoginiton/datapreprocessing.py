from directories import *

import numpy as np
import os
import cv2
from tqdm import tqdm
import random
import xml.etree.ElementTree as ET

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
        tree = ET.parse(os.path.join(ann_path, f"{img_name}.xml"))
        root = tree.getroot()

        print("Root:", root)

        for object in root.findall('object'):
            name = object.find('name').text
            class_categories.append(name)
    
    except Exception as e:
        print(f"Error parsing XML for image {img_name}: {e}")
        return []  # Return an empty list in case of errors
    
    return class_categories

def create_train_val_dataset():
    # Define the path to the dataset
    img_path = TRAIN_IMAGES
    for img in tqdm(os.listdir(img_path)):
        try:
            img_array = cv2.imread(os.path.join(img_path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
            new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize to normalize data size
            training_data.append([new_array, get_class_from_annotation(img[:-5], "train_val")])  # add this to our training_data
            print(get_class_from_annotation(img[:-5],"train_val"))
        except Exception as e:  # in the interest in keeping the output clean...
            pass
    random.shuffle(training_data)



def create_test_dataset():
    # Define the path to the dataset
    img_path = TEST_IMAGES

create_train_val_dataset()