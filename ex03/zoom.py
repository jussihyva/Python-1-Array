from load_image import ft_load
import numpy as np
from PIL import Image

def zoom_area() -> tuple:
    start_row:int = 120
    end_row:int = start_row + 400
    start_col:int = 450
    end_col:int = start_col + 400
    return (start_row, end_row, start_col, end_col)


def main(path:str) -> None:
    '''
    A program that load the image "animal.jpeg", print some information about it and display it after "zooming".
    '''
    image_array:np.ndarray = ft_load(path)
    if len(image_array) > 0:
        print(image_array)
        (start_row, end_row, start_col, end_col) = zoom_area()
        zoomed_image_array:np.ndarray = image_array[start_row:end_row, start_col:end_col, 0]
        zoomed_image:Image = Image.fromarray(zoomed_image_array)
        print('New shape after slicing: {}'.format(str(zoomed_image_array.shape)))
        zoomed_image.show()

if __name__ == '__main__':
    path:str = 'animal.jpeg'
    main(path)
