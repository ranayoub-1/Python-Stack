# 1 Countdown
def countdown(num):
    result = []
    for i in range(num, -1, -1):
        result.append(i)
    return result


# 2 Print and Return
def print_and_return(arr):
    print(arr[0])
    return arr[1]


# 3 First Plus Length
def first_plus_length(arr):
    return arr[0] + len(arr)


# 4 Values Greater than Second
def values_greater_than_second(arr):
    if len(arr) < 2:
        return False

    result = []
    for num in arr:
        if num > arr[1]:
            result.append(num)

    print(len(result))
    return result


# 5 This Length, That Value
def length_and_value(size, value):
    result = []
    for i in range(size):
        result.append(value)
    return result