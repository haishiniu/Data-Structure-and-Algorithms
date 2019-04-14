# -*- coding: utf-8 -*-
# !/usr/bin/python
"""
    Bubble sort, insertion sort and selection sort
    冒泡排序、插入排序、选择排序
    Author: haishiniu
"""


# 冒泡排序
def bubble_sort(a):
    length = len(a)
    if length <= 1:
        return

    for i in range(length):  # 循环的次数
        made_swap = False
        for j in range(length - i - 1):  # 每次循环比较的次数
            if a[j] > a[j + 1]:  # 前一个比后一个大交换位置(升序的方式【排列)
                a[j], a[j + 1] = a[j + 1], a[j]
                made_swap = True  # 交换成功标志位
        if not made_swap:  # 若交换标志位为False时候表示序列已经是升序
            break


# 插入排序(分已排序区和未排序区域)
def insertion_sort(a):
    length = len(a)
    if length <= 1:
        return
    # 为何从下标1开始？插入排序会把数据分成已近排序部分和未排序部分(下标为0的认为是已排序的部分，其余是未排序的部分)
    for i in range(1, length):
        value = a[i]
        j = i - 1
        while j >= 0 and a[j] > value:  # (是一种从有序数据部分最后开始向前比较的过程) 已经排序的数据部分与目前要排序的value进行循环大小比较
            a[j + 1] = a[j]  # 有序的最后一位向后移动一位
            j -= 1  # 下标向前在此比较
        a[j + 1] = value  # 已经排序部分的值


# 选择排序(分已排序区域和未排序区域)
def selection_sort(a):
    length = len(a)
    if length <= 1:
        return

    for i in range(length):
        min_index = i  # 最小值索引下标
        min_val = a[i]  # 最小值
        for j in range(i, length):  # 从剩余的数据中找最小数据
            if a[j] < min_val:
                min_val = a[j]  # 找到未排序中最小的元素
                min_index = j  # 找到未排序中最小元素对应的下标

        a[i], a[min_index] = a[min_index], a[i]  # 每经过一次i 就会有一个元素已经排序完成


def a_bubble_sort():
    test_array = [1, 1, 1, 1]
    bubble_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    bubble_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    bubble_sort(test_array)
    assert test_array == [1, 2, 3, 4]


def a_insertion_sort():
    test_array = [1, 1, 1, 1]
    insertion_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    insertion_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    insertion_sort(test_array)
    assert test_array == [1, 2, 3, 4]


def a_selection_sort():
    test_array = [1, 1, 1, 1]
    selection_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    selection_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    selection_sort(test_array)
    assert test_array == [1, 2, 3, 4]


if __name__ == "__main__":
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    bubble_sort(array)
    print(array)

    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    insertion_sort(array)
    print(array)

    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    selection_sort(array)
    print(array)
