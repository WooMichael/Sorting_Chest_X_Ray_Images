import pandas as pd
data = pd.read_csv("Chest_xray_Corona_Metadata.csv",index_col=0,header=0)
# image_name = list(data['X_ray_image_name'])
# class_type = list(data['Dataset_type'])
# label = list(data['Label'])
print(data['X_ray_image_name'])


