"""
File: blur.py
Name: Sanny Lin
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, smiley-face.png
    :return: SimpleImage, blurred smiley-face
    """
    # create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)

    # blurred
    for x in range(img.width):
        for y in range(img.height):
            # set variables (reset in each loop)
            red_sum, green_sum, blue_sum, count = 0, 0, 0, 0
            # get original pixels & calculate average
            for i in range(-1, 2, 1):  # x-1, x, x+1
                for j in range(-1, 2, 1):  # y-1, y, y+1
                    pixel_x = x + i
                    pixel_y = y + j
                    if 0 <= pixel_x < img.width and 0 <= pixel_y < img.height:
                        pixel = img.get_pixel(pixel_x, pixel_y)
                        red_sum += pixel.red
                        green_sum += pixel.green
                        blue_sum += pixel.blue
                        count += 1
            # set new_img pixel
            new_pixel = new_img.get_pixel(x, y)
            new_pixel.red = red_sum // count
            new_pixel.green = green_sum // count
            new_pixel.blue = blue_sum // count
    return new_img


def main():
    """
    blurred the smiley-face image
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
