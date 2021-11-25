import random
array = [(random.randint(1, 100)) for i in range(10)]
print(array)
array[array.index(min(array))], array[array.index(max(array))]\
    = array[array.index(max(array))], array[array.index(min(array))]
print(array)
