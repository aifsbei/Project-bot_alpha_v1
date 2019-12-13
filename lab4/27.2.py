from PIL import Image
import os


#def image_filter(pixels, i, j):
#    global image
#    low_color = (2, 43, 87)
#    high_color = (130, 190, 205)
#    r, g, b = 0, 0, 0
#    times = 1
#    for pixel in pixels:
#        if pixel is not image.getpixel((i, j)):
#            if low_color[0] < pixel[0] < high_color[0] and\
#                    low_color[1] < pixel[1] < high_color[1] and\
#                    low_color[2] < pixel[2] < high_color[2]:
#                r += pixel[0]
#                g += pixel[1]
#                b += pixel[2]
#                times += 1
#                print('times increased!111!')
#    return int(r/times), int(g/times), int(b/times)


def image_filter(pixels, i, j):
    """Заменяет цвет пикселя на цвет более холодного тона, тем самым
    переводит дневное изображение в ночное"""
    global image
    low_color = (2, 43, 87)
    high_color = (130, 190, 205)
    r, g, b = 0, 0, 0
    times = 1
    for pixel in pixels:
        if pixel is not image.getpixel((i, j)):
            r += pixel[0]
            g += pixel[1]
            b += pixel[2] * 1.3
            times += 1
    return int(r/times), int(g/times), int(b/times)


def select_pixels_around(pixel_coord, layers):
    global image
    width, height = image.size
    pixels_list = []
    for i in range(pixel_coord[0] - layers, pixel_coord[0] + layers):
        for j in range(pixel_coord[1] - layers, pixel_coord[1] + layers):
#            if pixel_coord[0] - layers < i < pixel_coord[1] + layers and\
#                    pixel_coord[0] - layers < j < pixel_coord[1] + layers:
            if pixel_coord[0] - layers > 0 and\
                pixel_coord[1] - layers > 0 and\
                pixel_coord[0] + layers < width and\
                pixel_coord[1] + layers < height:
                pixels_list.append(image.getpixel((i, j)))
#    pixels_list.append(image.getpixel((i, j)))
    return pixels_list


image = Image.open(os.getcwd() + '\\27.2_draws\\image.png')
img = image.load()
#image.save(os.getcwd() + '\\27.2_draws\\image.png', 'PNG')
w, h = image.size
#image = Image.new()
for i in range(w):
    for j in range(h):
        print('pixel {} {}:'.format(i, j))
        pixels = select_pixels_around((i, j), 1)
        img[i, j] = image_filter(pixels, i, j)
#pixels = select_pixels_around((0, 0), 5)
#img[0, 0] = image_filter(pixels, 0, 0)
image.show()
image.save(os.getcwd() + '\\27.2_draws\\new_image.png', 'PNG')