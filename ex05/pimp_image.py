import numpy as np
from PIL import Image

def invert_pixcel(pixcel:list) -> list:
    inverted_pixcel:list = np.array(list(map(lambda x: np.uint8(255) - x, pixcel)))
    return inverted_pixcel

def invert_row(row:list) -> list:
    inverted_row:np.ndarray = np.array(list(map(invert_pixcel, row)))
    return inverted_row


def red_pixcel(pixcel:np.ndarray) -> np.ndarray:
    red_color_pixcel:np.ndarray = np.array([
        pixcel[0],
        np.uint8(0),
        np.uint8(0)
    ])
    return red_color_pixcel


def green_pixcel(pixcel:np.ndarray) -> np.ndarray:
    red_color_pixcel:np.ndarray = np.array([
        np.uint8(0),
        pixcel[1],
        np.uint8(0)
    ])
    return red_color_pixcel


def blue_pixcel(pixcel:np.ndarray) -> np.ndarray:
    red_color_pixcel:np.ndarray = np.array([
        np.uint8(0),
        np.uint8(0),
        pixcel[2]
    ])
    return red_color_pixcel


def grey_pixcel(pixcel:np.ndarray) -> np.ndarray:
    value = np.mean(pixcel)
    red_color_pixcel:np.ndarray = np.array([
        np.uint8(value),
        np.uint8(value),
        np.uint8(value)
    ])
    return red_color_pixcel


def red_row(row:np.ndarray) -> np.ndarray:
    new_row:np.ndarray = np.array(list(map(red_pixcel, row)))
    return new_row


def green_row(row:np.ndarray) -> np.ndarray:
    new_row:np.ndarray = np.array(list(map(green_pixcel, row)))
    return new_row


def blue_row(row:np.ndarray) -> np.ndarray:
    new_row:np.ndarray = np.array(list(map(blue_pixcel, row)))
    return new_row


def grey_row(row:np.ndarray) -> np.ndarray:
    new_row:np.ndarray = np.array(list(map(grey_pixcel, row)))
    return new_row


def ft_invert(array:np.ndarray) -> np.ndarray:
    '''
    Invert picture colors
    '''
    new_array:np.ndarray = np.array(list(map(invert_row, array)))
    new_image:Image = Image.fromarray(new_array)
    new_image.show()
    return new_array

def ft_red(array:np.ndarray) -> np.ndarray:
    '''
    Red picture colors
    '''
    new_array:np.ndarray = np.array(list(map(red_row, array)))
    new_image:Image = Image.fromarray(new_array)
    new_image.show()
    return new_array


def ft_green(array:np.ndarray) -> np.ndarray:
    '''
    Green picture colors
    '''
    new_array:np.ndarray = np.array(list(map(green_row, array)))
    new_image:Image = Image.fromarray(new_array)
    new_image.show()
    return new_array


def ft_blue(array:np.ndarray) -> np.ndarray:
    '''
    Blue picture colors
    '''
    new_array:np.ndarray = np.array(list(map(blue_row, array)))
    new_image:Image = Image.fromarray(new_array)
    new_image.show()
    return new_array


def ft_grey(array:np.ndarray) -> np.ndarray:
    '''
    Gary picture colors
    '''
    new_array:np.ndarray = np.array(list(map(grey_row, array)))
    new_image:Image = Image.fromarray(new_array)
    new_image.show()
    return new_array

