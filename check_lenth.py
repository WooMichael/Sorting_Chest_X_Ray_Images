import os
# path, dirs, files = next(os.walk("Coronahack-Chest-XRay-Dataset/train_data_seperated_into_individual_folders/"))
# counter =  0
# for x in dirs:
#      print(x)
#      path, dirs, files = next(os.walk("Coronahack-Chest-XRay-Dataset/train_data_seperated_into_individual_folders/"+str(x)))
#      file_count = len(files)
#      print(file_count)
#      counter+=file_count
# print(counter)


path, dirs, files = next(os.walk("Coronahack-Chest-XRay-Dataset/test_data_seperated_into_individual_folders/"))
counter = 0
for x in dirs:
     print(x)
     path, dirs, files = next(os.walk("Coronahack-Chest-XRay-Dataset/test_data_seperated_into_individual_folders/"+str(x)))
     file_count = len(files)
     print(file_count)
     counter+=file_count
print(counter)


# print(file_count)
# path, dirs, files = next(os.walk("Coronahack-Chest-XRay-Dataset/test_data_seperated_into_individual_folders/Normal/"))
# file_count = len(files)
# print(file_count)
# path, dirs, files = next(os.walk("Coronahack-Chest-XRay-Dataset/test_data_seperated_into_individual_folders/Pnemonia bacteria"))
# file_count = len(files)
# print(file_count)
# path, dirs, files = next(os.walk("Coronahack-Chest-XRay-Dataset/test_data_seperated_into_individual_folders/Pnemonia Virus"))
# file_count = len(files)
# print(file_count)