import numpy as np
from PIL import Image
import PIL.ImageOps

def invert_pixcel(pixcel:list) -> list:
    inverted_pixcel:list = np.array(list(map(lambda x: np.uint8(255) - x, pixcel)))
    return inverted_pixcel

def invert_row(row:list) -> list:
    inverted_row:np.ndarray = np.array(list(map(invert_pixcel, row)))
    return inverted_row


def red_pixcel(pixcel:list) -> list:
    red_color_pixcel:list = np.array([
        np.uint8(255),
        pixcel[1],
        pixcel[2]
    ])
    return red_color_pixcel


def red_row(row:list) -> list:
    red_row:np.ndarray = np.array(list(map(red_pixcel, row)))
    # print('ROW: {}'.format(str(row)))
    # print('RED_ROW: {}'.format(str(red_row)))
    return red_row


def ft_invert(array:np.ndarray) -> np.ndarray:
    '''
    Invert picture colors
    '''
    inverted_array:np.ndarray = np.array(list(map(invert_row, array)))
    inverted_image:Image = Image.fromarray(inverted_array)
    inverted_image.show()

def ft_red(array:np.ndarray) -> np.ndarray:
    '''
    Red picture colors
    '''
    inverted_array:np.ndarray = np.array(list(map(red_row, array)))
    inverted_image:Image = Image.fromarray(inverted_array)
    inverted_image.show()


def ft_green(array:np.ndarray) -> np.ndarray:
    '''
    Green picture colors
    '''
    inverted_array:np.ndarray = np.array(list(map(invert, array)))
    inverted_image:Image = Image.fromarray(inverted_array)
    inverted_image.show()


def ft_blue(array:np.ndarray) -> np.ndarray:
    '''
    Blue picture colors
    '''
    inverted_array:np.ndarray = np.array(list(map(invert, array)))
    inverted_image:Image = Image.fromarray(inverted_array)
    inverted_image.show()


def ft_grey(array:np.ndarray) -> np.ndarray:
    '''
    Gary picture colors
    '''
    inverted_array:np.ndarray = np.array(list(map(invert, array)))
    inverted_image:Image = Image.fromarray(inverted_array)
    inverted_image.show()

