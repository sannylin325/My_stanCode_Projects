"""
File: mirror_lake.py
Name: Sanny Lin
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: mt-rainier.jpg
    :return: img, the lake with its reflection
    """
    img = SimpleImage('images/mt-rainier.jpg')
    r_img = SimpleImage.blank(img.width, img.height * 2)

    for x in range(img.width):
        for y in range(img.height):
            # copy and paste img to the upper-half of r_img
            # original pixel
            img_pixel = img.get_pixel(x, y)
            # blank pixel
            r_img_pixel = r_img.get_pixel(x, y)
            r_img_pixel.red = img_pixel.red
            r_img_pixel.green = img_pixel.green
            r_img_pixel.blue = img_pixel.blue

            # paste the up-side-down img to the lower-half of r_img
            r_img_pixel2 = r_img.get_pixel(x, r_img.height-1-y)
            r_img_pixel2.red = img_pixel.red
            r_img_pixel2.green = img_pixel.green
            r_img_pixel2.blue = img_pixel.blue
    return r_img


def main():
    """
    show the original image and the new image with reflection
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
