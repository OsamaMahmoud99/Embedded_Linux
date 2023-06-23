'''
Homework 1: 100 or 7?
● Write a program that reads an integer and print 100 if number is even or 7 if 
number is odd
○ E.g. for input 8 ⇒ 100
○ E.g. for input 133 ⇒ 7
'''

num = int(input())

is_even = num % 2 == 0

result = is_even * 100 + (not is_even) * 7

print(result)