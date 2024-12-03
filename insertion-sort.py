#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 00:29:03 2024

@author: emmanuel D Ramon
"""
#Algoritmo de insersion en un arrello

def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        current = i

        while current > 0 and arr[current - 1] > current_value:
            arr[current] = arr[current - 1]
            current -= 1

        arr[current] = current_value

arr = [5,1,8,61,87,2]

insertion_sort(arr)
print (arr)