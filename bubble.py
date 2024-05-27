#bubble sort 
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

def bubbleSort(list):
    while(1): # A loop to keep going until it is sorted
        swapped = False
        for j in range(len(list)-1): # the actual loop to compare the items
            if list[j] > list[j+1]:
                list[j], list[j + 1] = list[j + 1], list[j] # swapping adjacent items
                swapped = True
        if swapped is False: # if the loop goes through without any swaps then the list is sorted 
            return list

def is_sorted(lst):
    return lst == sorted(lst)

for list in list_of_lists:
    print(is_sorted(bubbleSort(list)))