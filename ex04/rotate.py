from load_image import ft_load
import numpy as np
from PIL import Image

def zoom_area() -> tuple:
    start_row:int = 120
    end_row:int = start_row + 400
    start_col:int = 450
    end_col:int = start_col + 400
    return (start_row, end_row, start_col, end_col)


def rotate_90_and_flip(array: np.array) -> np.ndarray:
    if len(array) > 0:
        row:list = list(array[0])
        rotated_image_array:np.ndarray = np.array(row)
        for row in array[1:]:
            rotated_image_array:np.ndarray = np.c_[rotated_image_array, row]
    else:
        rotated_image_array:np.ndarray = np.array([])
    return rotated_image_array


def main(path:str) -> None:
    '''
     A program which must load the image "animal.jpeg", cut a square part from it and transpose it to produce the image below.
     It should display it, print the new shape and the data of the image after the transpose.
    '''
    image_array:np.ndarray = ft_load(path)
    if len(image_array) > 0:
        (start_row, end_row, start_col, end_col) = zoom_area()
        zoomed_image_array:np.ndarray = image_array[start_row:end_row, start_col:end_col, 0]
        print('The shape of image is: {}'.format(zoomed_image_array.shape))
        print(zoomed_image_array)
        rotated_image_array:np.ndarray = rotate_90_and_flip(zoomed_image_array)
        print('New shape after Transpose: {}'.format(rotated_image_array.shape))
        print(rotated_image_array)
        try:
            transposed_image:Image = Image.fromarray(rotated_image_array)
            transposed_image.show()
        except Exception as e:
            print('{}: {}'.format(type(e).__name__, str(e)))

if __name__ == '__main__':
    path:str = 'animal.jpeg'
    main(path)
