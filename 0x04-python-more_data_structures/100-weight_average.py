#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    tu_mul = 0
    mul_sum = 0
    weight = 0
    for tu in my_list:
        tu_mul = tu[0] * tu[1]
        mul_sum += tu_mul
        weight += tu[1]
    result = mul_sum / weight
    return result
