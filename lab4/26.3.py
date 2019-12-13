from PIL import Image
import os


def select_channel(channel, img):
    pixels = img.load()
    x, y = img.size
    if channel == 'R':
        for i in range(x):
            for j in range(y):
                pixels[i, j] = (img.getpixel((i, j))[0], 0, 0)
    elif channel == 'G':
        for i in range(x):
            for j in range(y):
                pixels[i, j] = (0, img.getpixel((i, j))[1], 0)
    elif channel == 'B':
        for i in range(x):
            for j in range(y):
                pixels[i, j] = (0, 0, img.getpixel((i, j))[2])
    return img


def shift(img, delta):
    pixels = img.load()
    x, y = img.size
    for i in range(x):
        for j in range(y):
            try:
                pixels[i, j] = pixels[i + delta, j]
            except IndexError:
                pixels[i, j] = pixels[i + x - i - 1, j]
    return img


def change_brightness(img, percent):
    pixels = img.getdata()
    new_pixels = []
    multiplier = 1.0
    multiplier += (percent / 100.0)
    for pixel in pixels:
        new_pixel = (int(pixel[0] * multiplier),
                     int(pixel[1] * multiplier),
                     int(pixel[2] * multiplier))
        for value in new_pixel:
            if value > 255:
                value = 255
            elif value < 0:
                value = 0
        new_pixels.append(new_pixel)
    new_image = Image.new('RGB', img.size)
    new_image.putdata(new_pixels)
    return new_image

def makeanagliph(filename, delta):
    image = Image.open(os.getcwd() + '\\pict\\{}'.format(filename))
#    image = Image.new()###
#    r_channel = image.copy()
    r_channel = select_channel('R', image.copy())
    g_channel = select_channel('G', image.copy())
    b_channel = select_channel('B', image.copy())
#    temp = Image.New
    x, y = image.size
    gb_channel = Image.blend(g_channel, b_channel, 0.5)
    shifted_gb_channel = shift(gb_channel, delta).resize(image.size)
    rgb_channel = Image.blend(r_channel, shifted_gb_channel, 0.66)
    rgb_channel = change_brightness(rgb_channel, 200)
    rgb_channel.show()
    rgb_channel.save(os.getcwd() + '\\pict\\anagliph.png', 'PNG')


makeanagliph('draw.png', 10)