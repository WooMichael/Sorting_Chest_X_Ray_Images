# author: Michael Woo
import numpy as np
from sklearn import svm
from keras_preprocessing.image import ImageDataGenerator

# -----------path for training------------
train_path = 'Coronahack-Chest-XRay-Dataset/train_data_seperated_into_individual_folders'
test_path = 'Coronahack-Chest-XRay-Dataset/train_data_seperated_into_individual_folders'
print("Generating Image Data")
# ------------image data generator------------
train_datagen = ImageDataGenerator().flow_from_directory(train_path,target_size=(256, 256), batch_size=5286)
test_datagen = ImageDataGenerator().flow_from_directory(test_path,target_size=(256,256),batch_size=624)
# -------train_data----------
train_data, train_labels = next(train_datagen)
test_x, test_labels = next(test_datagen)
# train_data, train_labels = next(train_datagen)
# test_x, test_labels = next(test_datagen)

# print(train_datagen.filenames)
# train_file_names = train_datagen.filenames
# test_file_names = next(test_datagen)
# print(test_file_names)
# train_dia = list()
# test_dia = list()
# for x in train_file_names:
#     new_string = str(x)
#     reformat_string = new_string.split('\\')
#     train_dia.append(reformat_string.__getitem__(0))
# # print(train_dia)
# for x in test_file_names:
#     new_string = str(x)
#     reformat_string = new_string.split('\\')
#     test_dia.append(reformat_string.__getitem__(0))
# print(test_dia)
# ------------outputs---------
print("Reformating Image Data")
train_labels_y = np.array(train_labels)
train_labels_y = np.array([np.argmax(p) for p in train_labels_y])
test_labels = np.array(test_labels)
test_labels = np.array(([np.argmax(p) for p in test_labels]))
# print(train_labels_y)

# ------------inputs-----------
train_data_x = np.array(train_data)
test_x = np.array(test_x)
# -----------reshaping------------
X = train_data_x.reshape((-1, 256 * 256 * 3))
Y = train_labels_y
test_prediction = test_x.reshape((-1, 256 * 256 * 3))
# ------creating the model--------
print("Creating SVM Model...")
clf = svm.SVC(gamma='scale', decision_function_shape='ovo')
# --------Training the Model---------
print("Training Model...")
clf.fit(X, Y)
# --------Predictions-------------
print("Prediction..")
prediction_test = clf.predict(test_prediction)
# ---------Results that writes in file----------------
file = open("true_results.txt", "w")
print("-----Actual----------")
print(test_labels)
print("----Prediction-------")
print(prediction_test)
file.write("Actual"+"\n")
file.write(str(test_labels) + "\n")
file.write("Prediction" + "\n")
file.write(str(prediction_test))
file.close()
