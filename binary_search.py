__author__ = 'raihan'

import random


def binary_search(num_list, first, last, item):

    if len(num_list) == 0:
        return -1

    mid = int((first+last)/2)
    if num_list[mid] == item:
        return mid

    if first > last:
        return -1

    if item < num_list[mid]:
        return binary_search(num_list, first, mid-1, item)
    else:
        return binary_search(num_list, mid+1, last, item)

nums = [random.randint(1,10) for n in range(10)]
#nums = [1,3,5,7]
index = binary_search(nums, 0, 9, 5)
print(index)