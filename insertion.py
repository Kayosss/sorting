# insertion sort
import random
list_of_lists = [
    [random.randint(0, 100) for _ in range(10)],
    [random.randint(0, 100) for _ in range(10)],
    [random.randint(0, 100) for _ in range(10)],
    [random.randint(0, 100) for _ in range(10)],
    [random.randint(0, 100) for _ in range(10)],
    [random.randint(0, 100) for _ in range(10)],
    [random.randint(0, 100) for _ in range(10)],
    [random.randint(0, 100) for _ in range(10)],
    [random.randint(0, 100) for _ in range(10)],
    [random.randint(0, 100) for _ in range(10)]
]

def insertionSort(list):
    for i in range(1, len(list)):
        x = list[i] # the start of the unsorted portion of the array

        j = i -1 # the start of the sorted portion of the array
        while j >=0 and x < list[j]: # check if the unsorted element is bigger, looping through the sorted array to compare where it should be 
            list[j+1] = list[j] 
            j-=1
        list[j + 1] = x #
    print(list)
    return list


def is_sorted(lst):
    return lst == sorted(lst)

for list in list_of_lists:
    print(is_sorted(insertionSort(list)))