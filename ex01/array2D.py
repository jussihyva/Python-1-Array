import numpy as np

def are_input_values_valid(family:list, start: int, end: int):
    validation_result:bool = True
    if len(family) == 0:
        pass
    else:
        assert type(family[0]) == list, 'Content of the list is not list. Faulty type is {}'.format(str(type(family[0])))
        num_of_cols_in_the_first_list:int = len(family[0])
        try:
            faulty_num_of_columns:list = list(filter(lambda x: len(x) != num_of_cols_in_the_first_list, family))
            assert len(faulty_num_of_columns) == 0, 'List of list is not valid. there are list with different sizes. Check list lengths: {}'.format(str(family))
            np_family:np.ndarray = np.array(family)
            shape:tuple = np_family.shape
            min_value:int = -shape[0]
            max_value:int = shape[0] - 1
            assert start >= min_value and start <= max_value, 'Start value ({}) is not valid. Should be values between {} <= start => {}'.format(str(start), str(min_value), str(max_value))
            min_value:int = -shape[0]
            max_value:int = shape[0]
            assert end >= min_value and end <= max_value, 'End value ({}) is not valid. Should be values between {} <= end => {}'.format(str(end), str(min_value), str(max_value))
        except Exception as e:
            print('{}: {}'.format(type(e).__name__, str(e)))
            validation_result:bool = False
    return validation_result

def slice_me(family: list, start: int, end: int) -> list:
    if not are_input_values_valid(family, start, end):
        sliced_list:list = list()
    else:
        np_family:np.ndarray = np.array(family)
        shape:tuple = np_family.shape
        print('My shape is : {}'.format(str(shape)))
        step = 1
        np_sliced:np.ndarray = np_family[start:end:step]
        print('My new shape is : {}'.format(str(np_sliced.shape)))
        sliced_list:list = np_sliced.tolist()
    return sliced_list
