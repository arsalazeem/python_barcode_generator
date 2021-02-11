from PIL import Image, ImageDraw, ImageFilter


o_image = Image.open('blankimage.png')
svg_image = Image.open('somefile.jpeg')
o_image.paste(svg_image)
o_image.save("result.jpg")