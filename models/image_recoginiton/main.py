import tensorflow as tf

from model_train import train
from data_save import create_test_data

# Load test data
x_test, _ = create_test_data()

# Train the model
model = train()

# Make predictions
predictions = model.predict(x_test)

# Print the first prediction
print(predictions[0])