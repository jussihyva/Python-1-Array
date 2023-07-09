import numpy as np
from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile

def are_input_values_valid(path: str):
    validation_result:bool = True
    try:
        assert type(path) == str, 'Type of input parameter must be str. Now it is {}'.format(str(type(path)))
    except Exception as e:
        print('{}: {}'.format(type(e).__name__, str(e)))
        validation_result:bool = False
    return validation_result


def ft_load(path: str) -> np.ndarray:
    '''
    A function that loads an image, prints its format, and RETURN its pixels content in RGB format.
    '''
    image_array:np.ndarray = np.array([])
    if are_input_values_valid(path):
        try:
            image:JpegImageFile = Image.open(path)
            image_array:np.ndarray = np.asarray(image)
        except Exception as e:
            print('{}: {}'.format(type(e).__name__, str(e)))
    return image_array
