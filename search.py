def SearchIterative_1(ls, x):
    index = 0
    for i in ls:
        if i == x:
            return index
        index+=1
    return None

def SearchIterative_2(ls, x):
    for index, i in enumerate(ls):
        if i == x:
            return index
    return None

def binary_search_iterative(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return None
   
def binary_search_recursive(arr, x):
    if len(arr) == 0:
        return None;

    midindex = len(arr) // 2
    if (arr[midindex] == x):
        return midindex
    elif arr[midindex] > x:
        return binary_search_recursive(arr[:midindex], x)
    else: #arr[midindex] < x:
        retindex = binary_search_recursive(arr[midindex + 1:], x)
        if retindex == None:
            return None
        else:
            return midindex + 1 + retindex    

def binary_search_recursive2(arr, x, low, high):
    if high < low:
        return None;

    midindex = (high + low) // 2
    if (arr[midindex] == x):
        return midindex
    elif arr[midindex] > x:
        return binary_search_recursive2(arr, x, low, midindex - 1)
    else: #arr[midindex] < x:
        return binary_search_recursive2(arr, x, midindex + 1, high)