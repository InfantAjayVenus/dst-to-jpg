import os
import pyembroidery
from PIL import Image

def write_png(source_path, dest_path):
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    pattern = pyembroidery.read_dst(source_path)
    pyembroidery.write_png(pattern, dest_path)

def add_bg(path, fill_color=(0,0,0)):
    im = Image.open(path)
    im = im.convert("RGBA")
    if im.mode in ("RGBA", "LA"):
        background = Image.new(im.mode[:-1], im.size, fill_color)
        background.paste(im, im.split()[-1]) # omit transparency
        im = background
    im.convert("RGB").save(path)