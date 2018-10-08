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


timedelta_origin = timedelta(seconds=123456)

def timedelta_2_format_hms(timedelta_time_str):
    """将时间格式的字符串，转换为待显示的时间字符串
    example:
        input: 10:17:36
        output: 10h17m36s

    :param timedelta_time_str:
    :type string: timedelta_time_str
    :return:
    """
    print(timedelta_time_str)
    return_str = ""
    i = 0
    for time_item in timedelta_time_str.split(":"):
        if i == 0 and time_item != "0":
            return_str = time_item + "h"
        elif i == 1 and time_item != "00":
            return_str += (time_item + "m")
        elif i == 2 and time_item != "00":
            return_str += (time_item + "s")
        i += 1
    return return_str

def timedelta_2_format_dhms(origin_time_diff):
    """将时间差进行格式化转换
    example:
        input: timedelta(seconds=123456)
        output: 1d10h17m36s

    :param origin_time_diff: 时间差
    :type origin_time_diff: datetime.timedelta
    :return:
    :rtype string
    """
    if origin_time_diff <= timedelta(0):
        raise ValueError("'origin_time_diff=%s' cannot be less than 0" % str(origin_time_diff))
    time_str = str(origin_time_diff)
    if time_str.__contains__("days"):
        time_str_split_day = re.split('days, ', time_str)
        return str(int(time_str_split_day[0])) + "d" + timedelta_2_format_hms(time_str_split_day[1])
    elif time_str.__contains__("day"):
        time_str_split_day = re.split('day, ', time_str)
        return str(int(time_str_split_day[0])) + "d" + timedelta_2_format_hms(time_str_split_day[1])
    else:
        return timedelta_2_format_hms(time_str)
print(timedelta_origin)
print(timedelta_2_format_dhms(timedelta_origin))