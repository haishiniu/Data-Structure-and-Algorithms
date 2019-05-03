# -*- coding: utf-8 -*-
# !/usr/bin/python
"""
    Author: Wenru
"""
# 归并排序是个难点中的难点[理解 归 与 并 的这个过程]


def merge_sort(a):
    _merge_sort_between(a, 0, len(a) - 1)


def _merge_sort_between(a, low, high):
    """
    归并排序
    :param a:需排序数组 
    :param low: 最小下标
    :param high: 最大下标
    :return: 
    """
    if low < high:
        mid = low + (high - low) // 2
        _merge_sort_between(a, low, mid)
        _merge_sort_between(a, mid + 1, high)
        print(a, low, mid, high)
        _merge(a, low, mid, high)


def _merge(a, low, mid, high):

    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(a[start:end + 1])
    a[low:high + 1] = tmp


def a_merge_sort():
    a1 = [3, 5, 6, 7, 8]
    merge_sort(a1)
    assert a1 == [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    merge_sort(a2)
    assert a2 == [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    merge_sort(a3)
    assert a3 == [1, 2, 3, 4]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    merge_sort(a4)
    assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]


if __name__ == "__main__":
    a0 = [3, 2, 1, -2]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    merge_sort(a0)
    print(a0)

