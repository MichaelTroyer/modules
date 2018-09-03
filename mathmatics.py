# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 19:57:07 2018

@author: michael
"""

def findQuadraticRoots(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
    except ValueError:
        print 'Wrong input data type..'
    D = (b * b - 4 * a * c) ** 0.5
    x_1 = (-b + D) / (2 * a)
    x_2 = (-b - D) / (2 * a)
    return x_1, x_2

if __name__ == '__main__':
    a, b, c = 1, 1, 1
    print findQuadraticRoots(a, b, c)