'''
Homework 2: Fractional Part
● Write a program that reads 2 numbers a, b and divides them (a/b), but prints 
only the fraction part
● Input: 201 25
● Output: 0.04
○ Notice: 201 / 25 = 8.04
○ We only want the fraction part: 0.04
● Note:
○ Floats are approximations. So output like 0.039999999 is valid too
'''

a , b = map(int , input().split())

print( (a/b) - (a//b) )