#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 23:28:08 2024

@author: emmanuel
"""

#Nusqueda binaria


def binary_search(target: object, arr: list, start: int, end: int) -> bool:
    print(f'Searching {target} between {arr[start]} and {arr[end - 1]}')
    if start > end:
        return False

    middle = (start + end) // 2

    if arr[middle] == target:
        return True
    elif arr[middle] < target:
        return binary_search(arr, middle + 1, end, target)
    else:
        return binary_search(arr, start, middle - 1, target)
    
   
