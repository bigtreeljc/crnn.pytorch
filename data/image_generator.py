from captcha.image import ImageCaptcha
import glob
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

import random
import os

font_home = "/home/bigtree/Downloads/open-sans/"
# image = ImageCaptcha(fonts=glob.glob(font_home))
# 
# data = image.generate('AABHEO')
# image.write('AABHEO', 'out.png')

def test():
    sample = "This is a test"
    # sample1 = "哈哈，你输了"
    font_f = os.path.join(font_home, "OpenSans-SemiboldItalic.ttf")
    font = ImageFont.truetype(font_f, 14)
    width, height = font.getsize(sample)
    img=Image.new("RGBA", (width, height),(255,255,255))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), sample, (0,0,0), font=font)
    # width, height = draw.textsize(sample, font=font)
    print("w, h {}, {}".format(width, height))
    # img = img.resize((width, height), Image.ANTIALIAS)
    # draw.text((0, 0),"This is a test",(0,0,0),font=font)
    # draw = ImageDraw.Draw(img)
    img.save("a_test.png")

######
# right now only support english words
######
def gen_training_img(sample_str: str, target_loc: str):
    # sample = "This is a test"
    sample: str = sample_str
    font_f = os.path.join(font_home, "OpenSans-SemiboldItalic.ttf")
    font = ImageFont.truetype(font_f, 14)
    width, height = font.getsize(sample)
    img=Image.new("RGBA", (width, height),(255,255,255))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), sample, (0,0,0), font=font)
    print("w, h {}, {}".format(width, height))
    img.save(target_loc)

def gen_sample_str():
    pass

def gen_training_samples(n_samples):
    pass

