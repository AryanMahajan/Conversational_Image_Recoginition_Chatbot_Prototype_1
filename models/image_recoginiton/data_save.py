from datapreprocessing import *

train_data = create_train_val_dataset()
test_data = create_test_dataset()

x_train = []
x_test = []
y_train = []
y_test = []

def create_train_data():
    for x in train_data[0]:
        x_train.append(x)
    for y in train_data[1]:
        y_train.append(y)

    return x_train, y_train

def create_test_data():
    for x in test_data:
        x_test.append(x)
    for y in test_data:
        y_test.append(y)

    return x_test, y_test