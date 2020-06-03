# author: Michael Woo
import numpy as np
from sklearn import svm
from keras_preprocessing.image import ImageDataGenerator

# -----------path for training------------
train_path = 'Coronahack-Chest-XRay-Dataset/train_data_seperated_into_individual_folders'
test_path = 'Coronahack-Chest-XRay-Dataset/train_data_seperated_into_individual_folders'
# ------------image data generator------------
train_datagen = ImageDataGenerator().flow_from_directory(train_path,target_size=(32, 32), batch_size=5286)
test_datagen = ImageDataGenerator().flow_from_directory(test_path,target_size=(32, 32), batch_size=624, shuffle=False)
# -------train_data----------
train_data, train_labels = next(train_datagen)
test_x, test_labels = next(test_datagen)
# ------------outputs---------
train_labels_y = np.array(train_labels)
train_labels_y = np.array([np.argmax(p) for p in train_labels_y])
# ------------inputs-----------
train_data_x = np.array(train_data)
test_x = np.array(test_x)
# -----------reshaping------------
X = train_data_x.reshape((-1, 32 * 32 * 3))
Y = train_labels_y
test_prediction = test_x.reshape((-1, 32 * 32 * 3))
# ------creating the model--------
clf = svm.SVC(gamma='scale', decision_function_shape='ovo', verbose=False)
# --------Training the Model---------
clf.fit(X, Y)
# --------Predictions-------------
prediction_test = clf.predict(test_prediction)
# ---------Results that writes in file----------------
print(prediction_test)
