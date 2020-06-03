# author: Michael Woo
import numpy as np
from sklearn import svm
from keras_preprocessing.image import ImageDataGenerator

# -----------path for training------------
train_path = 'Coronahack-Chest-XRay-Dataset/train_data_seperated_into_individual_folders'
test_path = 'Coronahack-Chest-XRay-Dataset/train_data_seperated_into_individual_folders'
# ------------image data generator------------
train_datagen = ImageDataGenerator().flow_from_directory(train_path,target_size=(32, 32), batch_size=10)
test_datagen = ImageDataGenerator().flow_from_directory(test_path,target_size=(1000,1000),batch_size=5)
# -------train_data----------
# train_data, train_labels = next(train_datagen)
# test_x, test_labels = next(test_datagen)
train_data, train_labels = next(train_datagen)
test_x, test_labels = next(test_datagen)

# print(train_datagen.filenames)
train_file_names = train_datagen.filenames
test_file_names = test_datagen.filenames
train_dia = list()
test_dia = list()
for x in train_file_names:
    new_string = str(x)
    reformat_string = new_string.split('\\')
    train_dia.append(reformat_string.__getitem__(0))
# print(train_dia)
for x in test_file_names:
    new_string = str(x)
    reformat_string = new_string.split('\\')
    test_dia.append(reformat_string.__getitem__(0))
print(test_dia)
# # ------------outputs---------
# train_labels_y = np.array(train_labels)
# train_labels_y = np.array([np.argmax(p) for p in train_labels_y])
# # print(train_labels_y)
#
# # ------------inputs-----------
# train_data_x = np.array(train_data)
# test_x = np.array(test_x)
# # -----------reshaping------------
# X = train_data_x.reshape((-1, 32 * 32 * 3))
# Y = train_labels_y
# test_prediction = test_x.reshape((-1, 32 * 32 * 3))
# # ------creating the model--------
# clf = svm.SVC(gamma='scale', decision_function_shape='ovo', verbose=False)
# # --------Training the Model---------
# clf.fit(X, Y)
# # --------Predictions-------------
# prediction_test = clf.predict(test_prediction)
# # ---------Results that writes in file----------------
# print(prediction_test)
