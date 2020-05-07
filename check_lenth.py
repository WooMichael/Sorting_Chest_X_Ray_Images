import os
path, dirs, files = next(os.walk("Coronahack-Chest-XRay-Dataset/Train/Normal/"))
file_count = len(files)
print(file_count)