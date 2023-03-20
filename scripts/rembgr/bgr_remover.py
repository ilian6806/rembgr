from rembg import remove
from PIL import Image

def process(img):
    return remove(img)

def add_background(img, rgb_tuple):
    background_image = Image.new('RGB', img.size, rgb_tuple)
    background_image.paste(img, (0, 0), img)
    return background_image

def merge_images(img_list):
    result = Image.new('RGBA', img_list[0].size, (0, 0, 0, 0))
    for img in img_list:
        result.paste(img, (0, 0), mask=img)
        result.paste(result, (0, 0), mask=result.split()[3])
    return result
