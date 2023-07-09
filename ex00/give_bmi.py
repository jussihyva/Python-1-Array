from typing import Union
import numpy as np

def are_input_values_valid(height: list[Union[int, float]], weight: list[Union[int, float]]):
    validation_result:bool = True
    try:
        faulty_values = list(filter(lambda x: type(x) not in [float, int], height))
        assert len(faulty_values) == 0, 'Input values are not valid. All values should be int or/and float. Faulty values are: {}'.format(str(faulty_values))
        faulty_values = list(filter(lambda x: type(x) not in [float, int], weight))
        assert len(faulty_values) == 0, 'Input values are not valid. All values should be int or/and float. Faulty values are: {}'.format(str(faulty_values))
        assert len(height) == len(weight), 'Input values are not valid. Size of lists should be same. Now sizes are {} and {}'.format(str(len(height)), str(len(weight)))
    except Exception as e:
        print('{}: {}'.format(type(e).__name__, str(e)))
        validation_result:bool = False
    return validation_result

def give_bmi(height: list[Union[int, float]], weight: list[Union[int, float]]) -> list[Union[int, float]]:
# def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    bmi_list = list()
    if not are_input_values_valid(height, weight):
        pass
    else:
        np_height:np.ndarray = np.array(height)
        np_weight:np.ndarray = np.array(weight)
        np_height_squared:np.ndarray = np.power(np_height, 2)
        bmi_list:list = list(np.divide(np_weight, np_height_squared))
    return bmi_list

def apply_limit(bmi: list[Union[int, float]], limit: int) -> list[bool]:
# def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    limit_list = list(map(lambda x: x > limit, bmi))
    return limit_list
