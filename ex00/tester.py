from give_bmi import give_bmi, apply_limit

input_list = [
    { 'height': [2.71, 1.15], 'weight': [165.3, 38.4], 'is_valid_input': True },
    { 'height': [2.71, 1.15], 'weight': [165.3, '123'], 'is_valid_input': False },
    { 'height': [2.71, 'dsfsfdf'], 'weight': [165.3, '123'], 'is_valid_input': False },
    { 'height': [2.71, 1.15, 3], 'weight': [165.3, 38.4], 'is_valid_input': False },
]

test_case_id = -1
for input in input_list:
    test_case_id += 1
    if len(input['height']) == 0 and input['weight'] == 0:
        is_valid_result = True
    else:
        bmi = give_bmi(input['height'], input['weight'])
        if len(bmi) > 0:
            print(bmi, type(bmi))
            print(apply_limit(bmi, 26))
            is_valid_result = True
        else:
            is_valid_result = False
    test_case_result:bool = input['is_valid_input'] == is_valid_result
    print('Test case id: {}. Test result: {}'.format(str(test_case_id), str(test_case_result)))
