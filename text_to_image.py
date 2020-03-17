import arabic_reshaper
import pandas as pd
from string import punctuation
from bidi.algorithm import get_display
from PIL import Image, ImageDraw, ImageFont
import random

path = 'E:/Arabic OCR/يوميات شامية.csv'

df = pd.read_csv(path, encoding='utf-8')


def text_to_image():
    font_list = ["arialbd.ttf", "andlso.ttf", "majalla.ttf", "andlso.ttf", "trado.ttf"]

    for i, text in enumerate(df['text']):
        # keep only letters
        text = ''.join([c for c in text if c not in punctuation])
        text_to_be_reshaped = text
        reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)
        # At this stage the text is reshaped, all letters are in their correct form
        # based on their surroundings, but if you are going to print the text in a
        # left-to-right context, which usually happens in libraries/apps that do not
        # support Arabic and/or right-to-left text rendering, then you need to use
        # get_display from python-bidi.
        # Note that this is optional and depends on your usage of the reshaped text.
        bidi_text = get_display(reshaped_text)
        #
        # At this stage the text in bidi_text can be easily rendered in any library
        # that doesn't support Arabic and/or right-to-left, so use it as you'd use
        # any other string. For example if you're using PIL.ImageDraw.text to draw
        # text over an image you'd just use it like this...
        #
        # Here we can change the size and the font family
        font = ImageFont.truetype(random.choice(font_list), random.randrange(14, 60))
        image = Image.new('RGB', (800, 500), (255, 255, 255))
        image_draw = ImageDraw.Draw(image)
        image_draw.text((10, 10), bidi_text, fill=(0, 255, 0), font=font)
        # Now the text is rendered properly on the image, you can save it to a file or just call `show` to see it
        # working
        img_name = str(i + 1) + '.PNG'
        image.save(img_name)


if __name__ == "__main__":
    text_to_image()
