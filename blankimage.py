from PIL import Image


def create_image(name):
    img = Image.new("RGB", (192, 96), (255, 255, 255))
    img.save(name + ".png", "PNG")


if __name__ == '__main__':
    create_image("blankimage")


