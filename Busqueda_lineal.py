#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:25:56 2024

@author: emmanuel
"""

#Se define una busqueda para un arreglo lineal
def sequential_search(target: object, arr: list) -> bool:
    match = False

    for o in arr:
        if target is o:
            match = True
            break
            
    return match

