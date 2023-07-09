from array2D import slice_me

family_data_list:list = [
    { 'family': [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]], 'start': 0, 'end': 2, 'is_valid_input': True },
    { 'family': [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]], 'start': 1, 'end': -2,'is_valid_input': True },
    { 'family': [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]], 'start': 3, 'end': 4,'is_valid_input': True },
    { 'family': [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]], 'start': 0, 'end': 5,'is_valid_input': False },
    { 'family': [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]], 'start': 0, 'end': 4,'is_valid_input': True },
    { 'family': [[1.80, 78.4, 42.42], [2.15, 102.7, 42.42], [2.10, 98.5, 42.42], [1.88, 75.2]], 'start': 0, 'end': 4,'is_valid_input': False },
    { 'family': [[1.80, 78.4, 42.42], [2.15, 102.7, 42.42], [2.10, 98.5, 42.42], [1.88, 75.2, 'String']], 'start': 0, 'end': 4,'is_valid_input': True },
]

test_case_id = -1
for family_data in family_data_list:
    test_case_id += 1
    family:list = family_data['family']
    start:int = family_data['start']
    end:int = family_data['end']
    sliced_list = slice_me(family, start, end)
    print('{}'.format(sliced_list))
    if len(sliced_list) > 0:
        is_valid_result = True
    else:
        is_valid_result = False
    test_case_result:bool = family_data['is_valid_input'] == is_valid_result
    print('Test case id: {}. Test result: {}'.format(str(test_case_id), str(test_case_result)))
print(slice_me.__doc__)