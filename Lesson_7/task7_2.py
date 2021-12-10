from random import randint


def array_gen(start, end, amount):
    array = []
    for i in range(amount):
        array.append(randint(start, end))
    return array


def array_sort(array):
    if len(array) == 1:
        return array[:]
    else:
        middle = len(array) // 2
        left = array_sort(array[:middle])
        right = array_sort(array[middle:])
        return array_merge(left, right)


def array_merge(left, right):
    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            res.append(right[j])
            j += 1
        else:
            res.append(left[i])
            i += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


array = array_gen(-100, 100, 15)

print(array)
print(array_sort(array))
