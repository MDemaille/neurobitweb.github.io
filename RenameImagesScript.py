import os
path = r"C:\Users\maxim\Documents\GitHub\neurobitweb.github.io\images"
files = os.listdir(path)

for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), 'dumi.bmp'])))

files = os.listdir(path)

for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.bmp'])))