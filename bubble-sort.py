#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 23:32:28 2024

@author: Emmanuel D Ramon
"""
 
#bubble sort
def burble_sort(arr):
    n=len(arr)    
    for i in range(n-1):
        for j in range (0, n-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j +1] , arr[j]
    
    return arr
arreglo = [1,5,9,7,4,2]
burble_sort(arreglo)

print(arreglo)
                
