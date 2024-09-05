# Python code​​​​​​‌​‌‌‌​‌​‌‌​​​​‌​‌‌​‌​‌​‌​ below
import itertools


def encodeString(stringVal):
    # Your code goes here.
    result = []
    for char, group in itertools.groupby(stringVal):
        count = len(list(group))
        result.append((char, count))
    return result


def decodeString(encodedList):
    # Your code goes here.
    result = ""
    for k, v in encodedList:
        result += k * v
    return result
