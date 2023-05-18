#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
	map_mul = map(lambda x: x * number, my_list)
    return list(map_mul)
