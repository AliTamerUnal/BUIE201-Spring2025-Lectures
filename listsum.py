def ListSum(x):
    sum = 0
    for i in x:
        sum += i
    return sum

def ListSumRecursive(x):
    if not x:
        return 0
    return x[0] + ListSumRecursive(x[1:])

ListSumRecursive([3,6,9])