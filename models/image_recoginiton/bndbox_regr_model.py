import tensorflow as tf

from data_save import create_train_data

x_train, y_train, bbox_train = create_train_data()

def bndbox_regression():
    bbox_model = tf.keras.Sequential()
    bbox_model.add(tf.keras.layers.Dense(4, activation='linear'))
    bbox_model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate = 0.001), loss = 'mse')
    bbox_model.fit(x_train, bbox_train,batch_size = 32, epochs = 20, validation_split = 0.2)
    return bbox_model