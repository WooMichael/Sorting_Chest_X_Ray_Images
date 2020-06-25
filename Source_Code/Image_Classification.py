# author: Michael Woo
import os
import numpy as np
from sklearn import svm
from keras_preprocessing.image import ImageDataGenerator
from PIL import Image
from sklearn.neighbors import KNeighborsClassifier
# -----------path for training------------
train_path = '../Coronahack-Chest-XRay-Dataset/train_data_seperated_into_individual_folders'
test_path = '../Coronahack-Chest-XRay-Dataset/test_data_seperated_into_individual_folders'
print("Generating Image Data")
width_image = list()
height_image = list()
#get all the sizes of images
files = os.listdir(train_path)
for directory in files:
    path = train_path + "/" + directory
    print(path)
    image_dir = os.listdir(path)
    print(image_dir)
    for im in image_dir:
        im_path = path + "/" + im
        what = Image.open(im_path)
        width, height = what.size
        width_image.append(int(width))
        height_image.append(int(height))
        print(width, height)
print("width min = "+ str(min(width_image)))
print("height min = " + str(min(height_image)))

print(files)


#exit(212354)
# ------------image data generator------------
train_datagen = ImageDataGenerator().flow_from_directory(train_path, batch_size=5286)
test_datagen = ImageDataGenerator().flow_from_directory(test_path,batch_size=624)
# -------train_data----------
train_data, train_labels = next(train_datagen)
test_x, test_labels = next(test_datagen)
# ------------outputs---------
print("Reformating Image Data")
train_labels_y = np.array(train_labels)
train_labels_y = np.array([np.argmax(p) for p in train_labels_y])
test_labels = np.array(test_labels)
test_labels = np.array(([np.argmax(p) for p in test_labels]))
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
file = open("../true_results.txt", "w")
filetwo = open("../prediction_results.txt", "w")
print("-----Actual----------")
print(test_labels)
print("----Prediction-------")
print(prediction_test)
for tl in test_labels:
    file.write(str(tl) + ",")
for pred in prediction_test:
    filetwo.write(str(pred) + ",")
file.close()
filetwo.close()
