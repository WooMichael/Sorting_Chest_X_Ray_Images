# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from keras_preprocessing.image import ImageDataGenerator
import numpy as np
# -----------path for training------------
train_path = 'Coronahack-Chest-XRay-Dataset/train_data_seperated_into_individual_folders'
test_path = 'Coronahack-Chest-XRay-Dataset/train_data_seperated_into_individual_folders'
# ------------image data generator------------
train_datagen = ImageDataGenerator().flow_from_directory(train_path,target_size=(256, 256), batch_size=50)
test_datagen = ImageDataGenerator().flow_from_directory(test_path,target_size=(256,256),batch_size=)
# -------train_data----------
train_data, train_labels = next(train_datagen)
test_x, test_labels = next(test_datagen)
# ------------outputs---------
train_labels_y = np.array(train_labels)
train_labels_y = np.array([np.argmax(p) for p in train_labels_y])
# ------------inputs-----------
train_data_x = np.array(train_data)
test_x = np.array(test_x)
model = keras.Sequential([
    keras.layers.Flatten(),
    keras.layers.Dense(256,activation='sigmoid',input_dim=1024*3),
    # keras.layers.Flatten(),
    # keras.layers.Dense(256*256,input_dim=1024*3),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(7)
])
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.fit(train_data_x, train_labels_y, epochs=20)

test_loss, test_acc = model.evaluate(test_x,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)