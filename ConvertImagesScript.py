from PIL import Image
import os

path = r"C:\Users\maxim\Documents\GitHub\neurobitweb.github.io\images"
images= os.listdir(path)
for img in images:
    Image.open(path+"\\"+img).save(os.path.join(path+ str(img).replace(".bmp",".jpg") + '.jpg'))