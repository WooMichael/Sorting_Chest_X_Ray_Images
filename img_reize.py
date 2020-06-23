from PIL import Image
image = Image.open('Metadata/Coronahack-Chest-XRay-Dataset/test/IM-0001-0001.jpeg')
new_image  = image.resize((100,100))
new_image.save('got_img.jpeg')
new_image.show()