# import logging
# import functools
# def debug(level):
#     def mydecorator(f):
#         @functools.wraps(f)
#         def log_f_as_called(*args, **kwargs):
#             logging.log(level, f'{f} was called with arguments={args} and kwargs={kwargs}')
#             value = f(*args, **kwargs)
#             logging.log(level, f'{f} return value {value}')
#             return value
#         return log_f_as_called
#     return mydecorator
#
# @debug(level="info")
# def hello():
#     print("hello")
#
# hello()

# def quicksort(array):
#     less = []
#     greater = []
#     if len(array) <= 1:
#         return array
#     pivot = array.pop()
#     for x in array:
#         if x <= pivot:
#             less.append(x)
#         else:
#             greater.append(x)
#     return quicksort(less)+[pivot]+quicksort(greater)
#
# print(quicksort([4, 5, 1, 3, 9, 2]))

from datetime import datetime, timedelta
import re


time_str = str(timedelta(seconds=3600))

def get_time_str_by_symbol(time_str):
    return_str = ""
    i = 0
    for time_item in time_str.split(":"):
        if i == 0 and time_item != "0":
            return_str = time_item + "h"
        elif i == 1 and time_item != "00":
            return_str += (time_item + "m")
        elif i == 2 and time_item != "00":
            return_str += (time_item + "s")
        i += 1
    return return_str

def get_time(time_str):
    if time_str.__contains__("days"):
        time_str_split_day = re.split('days, ', time_str)
        return str(int(time_str_split_day[0])) + "d" + get_time_str_by_symbol(time_str_split_day[1])
    elif time_str.__contains__("day"):
        time_str_split_day = re.split('day, ', time_str)
        return str(int(time_str_split_day[0])) + "d" + get_time_str_by_symbol(time_str_split_day[1])
    else:
        return get_time_str_by_symbol(time_str)
print(time_str)
print(get_time(time_str))