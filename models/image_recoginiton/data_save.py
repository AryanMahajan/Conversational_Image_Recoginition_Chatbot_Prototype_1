from datapreprocessing import *
import numpy as np

train_data = create_train_val_dataset()
test_data = create_test_dataset()

x_train = np.array()
x_test = np.array()
y_train = np.array()
y_test = np.array()

for d in train_data:
    np.append(x_train, d[0])
    np.append(y_train, [d[1],d[2]])

for d in test_data:
    np.append(x_test, d[0])
    np.append(y_test, [d[1],d[2]])

np.save('X_train.npy', x_train)
np.save('y_train.npy', y_train)
np.save('X_test.npy', x_test)
np.save('y_test.npy', y_test)