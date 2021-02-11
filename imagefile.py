from PIL import Image

image = Image.open('filename.png')
# new_image = image.resize((192, 96))
image.save("image.png")
print(image.size)