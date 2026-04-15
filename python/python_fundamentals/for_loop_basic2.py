# 1 Biggie Size
def biggie_size(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr


# 2 Count Positives
def count_positives(arr):
    count = 0
    for num in arr:
        if num > 0:
            count += 1
    arr[-1] = count
    return arr


# 3 Sum Total
def sum_total(arr):
    total = 0
    for num in arr:
        total += num
    return total


# 4 Average
def average(arr):
    total = sum_total(arr)
    return total / len(arr)


# 5 Length
def length(arr):
    count = 0
    for _ in arr:
        count += 1
    return count


# 6 Minimum
def minimum(arr):
    if len(arr) == 0:
        return False

    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val


# 7 Maximum
def maximum(arr):
    if len(arr) == 0:
        return False

    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val


# 8 Ultimate Analysis
def ultimate_analysis(arr):
    return {
        "sumTotal": sum_total(arr),
        "average": average(arr),
        "minimum": minimum(arr),
        "maximum": maximum(arr),
        "length": length(arr)
    }


# 9 Reverse List
def reverse_list(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr