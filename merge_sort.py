#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 00:32:46 2024

@author: Emmanuel D Ramon
"""
#Algoritmo de ordenamiento por fusion/mezcla

def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        print(left, '*' * 5, right)
    
        # llamada recursiva en cada mitad
        merge_sort(left)
        merge_sort(right)
    
        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para lista principal
        k = 0
    
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    
        print(f'left {left}, right {right}')
        print(arr)
        print('-' * 50)
    return arr

arr=[5,6,1,2,-4,15]
merge_sort(arr)

print (arr)