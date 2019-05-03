# -*- coding: utf-8 -*-
# !/usr/bin/python
"""
    Author: haishiniu
"""


def bsearch(nums, target):
    """Binary search of a target in a sorted array
    without duplicates. If such a target does not exist,
    return -1, othewise, return its index.
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    a1 = [1, 1.4, 3, 4]
    a = bsearch(a1, 3)
    print(a)