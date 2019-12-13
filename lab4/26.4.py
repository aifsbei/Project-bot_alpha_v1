from PIL import Image, ImageDraw
import os


def letter_d():
    letter = Image.new('RGB', (200, 200))
    draw = ImageDraw.Draw(letter)
    draw.rectangle([(50, 20), (80, 180)], fill=(255, 0, 0))
    draw.chord([(50, 20), (150, 180)], start=-90, end=-270, fill=(100, 150, 50), width=30)
    draw.ellipse([(85, 50), (120, 150)], fill='black')
    return letter


def letter_a():
    letter = Image.new('RGB', (200, 200), color='white')
    draw = ImageDraw.Draw(letter)
    draw.line([(50, 180), (100, 20)], fill=(20, 200, 190), width=30)
    draw.line([(100, 20), (150, 180)], fill=(20, 200, 190), width=30)
    draw.ellipse([(85, 135), (115, 165)], fill=(120, 20, 230))
    return letter


def letter_n():
    letter = Image.new('RGB', (200, 200))
    draw = ImageDraw.Draw(letter)
    draw.line([(65, 26), (135, 174)], fill=(70, 200, 200), width=30)
    draw.rectangle([(50, 20), (80, 180)], fill=(230, 140, 190))
    draw.rectangle([(120, 20), (150, 180)], fill=(120, 250, 10))
    return letter

def draw_name():
    image = Image.new('RGB', (600, 200))
    image.paste(letter_d(), (0, 0))
    image.paste(letter_a(), (200, 0))
    image.paste(letter_n(), (400, 0))
    image.save(os.getcwd() + '\\26.4_draws\\name.png', 'PNG')
    image.show()


draw_name()