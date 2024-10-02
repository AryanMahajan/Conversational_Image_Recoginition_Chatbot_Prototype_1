import tensorflow as tf
import numpy as np

from data_save import create_train_data
from model import define_compile_model

# Load training data
X_train, y_train = create_train_data()

def train():
  # Define the model input shape based on the training data
  input_shape = np.array(X_train).shape[1:]  # Get the shape excluding the batch dimension

  # Create and compile the model
  model = define_compile_model(tf.keras.layers.Input(shape=input_shape))
  model.fit(X_train, y_train, epochs=10, validation_split=0.2)

  model.save('model.keras')

  return model