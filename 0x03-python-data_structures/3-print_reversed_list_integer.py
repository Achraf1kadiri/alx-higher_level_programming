#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return

    my_list.reverse()
    length = len(my_list)
    i = 0

    while i < length:
        print('{:d}'.format(my_list[i]))
        i += 1
