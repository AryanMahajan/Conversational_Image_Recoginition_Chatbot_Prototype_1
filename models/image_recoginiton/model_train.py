import tensorflow as tf

from data_save import create_train_data
from model import define_compile_model

X_train, y_train = create_train_data()

def train():
    model = define_compile_model(tf.keras.layers.Input(100,100,1))
    history = model.fit(X_train, y_train, epochs=10, validation_split= 0.2)
    model.save('model.h5')

train()