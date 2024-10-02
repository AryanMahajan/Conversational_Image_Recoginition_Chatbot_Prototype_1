import tensorflow as tf

from data_save import create_train_data

x_train, y_train, _ = create_train_data()

base_model = tf.keras.applications.resnet.ResNet50(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
base_model.trainable = False
NUM_FILTERS = 512

def classification_model():
    class_model = tf.keras.Sequential()
    class_model.add(base_model)
    class_model.add(tf.keras.layers.Conv2D(NUM_FILTERS,(3,3),padding='same', kernel_initializer='he_normal'))
    class_model.add(tf.keras.layers.BatchNormalization())
    class_model.add(tf.keras.layers.LeakyReLU(alpha=0.1))

    class_model.add(tf.keras.layers.Conv2D(NUM_FILTERS,(3,3),padding='same', kernel_initializer='he_normal'))
    class_model.add(tf.keras.layers.BatchNormalization())
    class_model.add(tf.keras.layers.LeakyReLU(alpha=0.1))

    class_model.add(tf.keras.layers.Conv2D(NUM_FILTERS,(3,3),padding='same', kernel_initializer='he_normal'))
    class_model.add(tf.keras.layers.BatchNormalization())
    class_model.add(tf.keras.layers.LeakyReLU(alpha=0.1))

    class_model.add(tf.keras.layers.Flatten())

    class_model.add(tf.keras.layers.Dense(NUM_FILTERS,kernel_initializer='he_normal'))
    class_model.add(tf.keras.layers.BatchNormalization())
    class_model.add(tf.keras.layers.LeakyReLU(alpha=0.1))

    class_model.add(tf.keras.layers.Dense(20, activation = 'sigmoid'))

    class_model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate = 0.001), loss = 'sparse_categorical_crossentropy', metrics=["accuracy"])

    class_model.fit(x_train, y_train, batch_size = 32, epochs = 20, validation_split = 0.2)

    return class_model