import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from datapreprocessing import *
from model import define_compile_model

train_data = create_train_val_dataset()
test_data = create_test_dataset()

x_train = []
x_test = []
y_train = []
y_test = []

for d in train_data:
    x_train.append(d[0])
    y_train.append([d[1],d[2]])

for d in test_data:
    x_test.append(d[0])
    y_test.append([d[1],d[2]])


model = define_compile_model(tf.keras.layers.Input(shape = (100,100,1)))
history = model.fit(x_train,y_train,epochs = 20)