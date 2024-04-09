# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:52:09 2024

@author: user
"""

print('выберите один из вариантов: 1. круг 2. прямоугольник 3. треугольник')
f = input('напишите порядковый номер типа фигуры: ')
if f == '1':
    r = int(input("r = "))
    s = (r ** 2) * 3.14
    print('площадь круга:',s)
elif f == '2':
    a = int(input('a = '))
    b = int(input('b = '))
    s = a * b
    print('площадь прямоугольника:',s)
elif f == '3':
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c))**(1/2)
    if c == (a*a + b*b)**(1/2):
        print('площадь прямоугольного треугольника:', s)
    else:
        print('площадь треугольника:', s)