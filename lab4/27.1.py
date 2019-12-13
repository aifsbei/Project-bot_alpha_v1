from PIL import Image
import os


def make_preview(size, quantize_multiplier):
    image = Image.open(os.getcwd() + '\\27.1_draws\\image.jpg')
    image = image.resize(size, resample=Image.BILINEAR)
    image = image.quantize(quantize_multiplier)
    image.save(os.getcwd() + '\\27.1_draws\\new_image.bmp', 'BMP')
    image.show()


make_preview((400, 200), 10)