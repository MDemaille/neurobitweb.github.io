#!/usr/bin/python
from PIL import Image
import os, sys

path = r"C:\Users\maxim\Documents\GitHub\neurobitweb.github.io\images"
dirs = os.listdir(path)

def resize():
    for item in dirs:
        im = Image.open(path+"\\"+item)
        f, e = os.path.splitext(path+"\\"+item)
        imResize = im.resize((320,240))
        imResize.save(f + '.jpg', 'JPEG', quality=90)

resize()