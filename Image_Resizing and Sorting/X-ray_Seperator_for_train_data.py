import pandas as pd
from shutil import copyfile

data = pd.read_csv("../Metadata/Chest_xray_Corona_Metadata.csv", index_col=0, header=0)
image_name = list(data['X_ray_image_name'])
class_type = list(data['Dataset_type'])
label = list(data['new_label'])
tri_tuple = list()
i = 0
while i < len(image_name):
    tri_tuple.append((image_name.__getitem__(i), label.__getitem__(i), class_type.__getitem__(i)))
    i += 1
for pup in tri_tuple:
    if (pup.__getitem__(2) == 'TRAIN' and pup.__getitem__(1) == 'Normal  '):
        copyfile('Coronahack-Chest-XRay-Dataset/Coronahack-Chest-XRay-Dataset/train/' + pup.__getitem__(0),
                 'Coronahack-Chest-XRay-Dataset/train_data_seperated_into_individual_folders/Normal/' + pup.__getitem__(0))
    if (pup.__getitem__(2) == 'TRAIN' and pup.__getitem__(1) == 'Pnemonia  bacteria'):
        copyfile('Coronahack-Chest-XRay-Dataset/Coronahack-Chest-XRay-Dataset/train/' + pup.__getitem__(0),
                 'Coronahack-Chest-XRay-Dataset/train_data_seperated_into_individual_folders/Pnemonia bacteria/' + pup.__getitem__(0))
    if (pup.__getitem__(2) == 'TRAIN' and pup.__getitem__(1) == 'Pnemonia Streptococcus bacteria'):
        copyfile('Coronahack-Chest-XRay-Dataset/Coronahack-Chest-XRay-Dataset/train/' + pup.__getitem__(0),
                 'Coronahack-Chest-XRay-Dataset/train_data_seperated_into_individual_folders/Pnemonia bacteria Streptococcus/' + pup.__getitem__(0))
    if (pup.__getitem__(2) == 'TRAIN' and pup.__getitem__(1) == 'Pnemonia ARDS Stress-Smoking'):
        copyfile('Coronahack-Chest-XRay-Dataset/Coronahack-Chest-XRay-Dataset/train/' + pup.__getitem__(0),
                 'Coronahack-Chest-XRay-Dataset/train_data_seperated_into_individual_folders/Pnemonia Stress-Smoking ARDS/' + pup.__getitem__(0))
    if (pup.__getitem__(2) == 'TRAIN' and pup.__getitem__(1) == 'Pnemonia  Virus'):
        copyfile('Coronahack-Chest-XRay-Dataset/Coronahack-Chest-XRay-Dataset/train/' + pup.__getitem__(0),
                 'Coronahack-Chest-XRay-Dataset/train_data_seperated_into_individual_folders/Pnemonia Virus/' + pup.__getitem__(0))
    if (pup.__getitem__(2) == 'TRAIN' and pup.__getitem__(1) == 'Pnemonia COVID-19 Virus'):
        copyfile('Coronahack-Chest-XRay-Dataset/Coronahack-Chest-XRay-Dataset/train/' + pup.__getitem__(0),
                 'Coronahack-Chest-XRay-Dataset/train_data_seperated_into_individual_folders/Pnemonia Virus COVID-19/' + pup.__getitem__(0))
    if (pup.__getitem__(2) == 'TRAIN' and pup.__getitem__(1) == 'Pnemonia SARS Virus'):
        copyfile('Coronahack-Chest-XRay-Dataset/Coronahack-Chest-XRay-Dataset/train/' + pup.__getitem__(0),
                 'Coronahack-Chest-XRay-Dataset/train_data_seperated_into_individual_folders/Pnemonia Virus SARS/' + pup.__getitem__(0))
# print(label)
# print(image_name)
# print(class_type)
