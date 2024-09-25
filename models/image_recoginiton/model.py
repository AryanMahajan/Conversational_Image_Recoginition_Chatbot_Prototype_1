import tqdm
import tensorflow as tf
from keras_resnet.models import ResNet50
import numpy as np
import os

def feature_extractor(inputs):
    
    return ResNet50(input_shape = (100, 100, 3), include_top = False, weights = 'imagenet')(inputs)

def bndbox_coordinate_regression(inputs):
    return tf.keras.layers.Dense(4, name = 'bounding_box')(inputs)

def classifier(inputs):
    return tf.keras.layers.Dense(20, activation = 'softmax', name = 'classification')(inputs)

def dense_layers(inputs):
    x = tf.keras.layers.Flatten()(inputs)
    x = tf.keras.layers.Dense(128, activation = 'relu')(x)
    return x

def final_model(inputs):
    feature_cnn = feature_extractor(inputs)
    dense_output = dense_layers(feature_cnn)

    classification_output = classifier(dense_output)
    bndbox_coordinate_regression_output = bndbox_coordinate_regression(dense_output)

    model = tf.keras.Model(inputs = inputs, outputs = [classification_output, bndbox_coordinate_regression_output])
    return model


def define_compile_model(inputs):
    model = final_model(inputs)
    model.compile(optimizer = 'adam', 
                  loss = {'classification': 'sparse_categorical_crossentropy', 'bounding_box': 'mse'},
                  metrics = {'classification' : 'accuracy', 'bounding_box' : 'mse'}
    )
    return model

