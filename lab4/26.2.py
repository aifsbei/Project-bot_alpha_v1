from PIL import Image, ImageDraw
import random

def board(dimension, pixel_size):
    board_color = (255, 255, 255)
    w = dimension * pixel_size
    image = Image.new('RGB', (w, w), board_color)
    draw = ImageDraw.Draw(image)
    colors = set()
    while len(colors) < dimension * dimension:
        r = random.randint(0, 256)
        g = random.randint(0, 256)
        b = random.randint(0, 256)
        colors.add((r, g, b))
    for i in range(dimension):
        for j in range(dimension):
            shape = [(i * pixel_size, j * pixel_size), ((i + 1) * pixel_size, (j + 1) * pixel_size)]
            draw.rectangle(shape, fill=(colors.pop()))
    image.save('chess.png', 'PNG')
    image.show()


board(8, 50)