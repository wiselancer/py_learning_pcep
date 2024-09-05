def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 0
    elif type(num) is int and num > 1:
        result = 1
        for i in range(1, num + 1):
            result = result * i
        return result
    else:
        return None


def factorial2(num):
    if type(num) is not int or num < 0:
        return None
    return num * factorial2(num - 1) if num > 0 else 1
