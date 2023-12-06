#!/usr/bin/python3
def uniq_add(my_list=[]):
    result_set = set()
    for item in my_list:
        result_set.add(item)
    return sum(result_set)
