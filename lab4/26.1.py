from PIL import ImageDraw, Image
import os
import time

x = 512
y = 200


def gradient(color):
    new_color = (0, 0, 0)
    new_image = Image.new('RGB', (x, y), new_color)
    draw = ImageDraw.Draw(new_image)
    if color == 'R':
        for i in range(256):
            draw.line((i * 2, 0, i * 2, y), fill=(i, 0, 0), width=2)
    elif color == 'G':
        for i in range(256):
            draw.line((i * 2, 0, i * 2, y), fill=(0, i, 0), width=2)
    elif color == 'B':
        for i in range(256):
            draw.line((i * 2, 0, i * 2, y), fill=(0, 0, i), width=2)
    new_image.save(os.getcwd() + '\\26.1_draws\\draw' + str(int(time.time())) + '.png', 'PNG')
    new_image.show()


gradient('G')