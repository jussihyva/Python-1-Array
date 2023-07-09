from load_image import ft_load
import numpy as np

image_data_list:list = [
    { 'image_path': 'landscape.jpg', 'is_valid_input': True },
    { 'image_path': 'load_image.py', 'is_valid_input': False },
    { 'image_path': 'no_file', 'is_valid_input': False },
    { 'image_path': True, 'is_valid_input': False },
    { 'image_path': 2, 'is_valid_input': False },
    { 'image_path': 'animal.jpeg', 'is_valid_input': True },
]


test_case_id = -1
for image_data in image_data_list:
    test_case_id += 1
    path:str = image_data['image_path']
    image_array:np.ndarray = ft_load(path)
    if len(image_array) > 0:
        is_valid_result = True
    else:
        is_valid_result = False
    test_case_result:bool = image_data['is_valid_input'] == is_valid_result
    print('Test case id: {}. Test result: {}'.format(str(test_case_id), str(test_case_result)))
