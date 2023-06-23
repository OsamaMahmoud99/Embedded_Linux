'''
Homework 2: Last 3 digits sum
● Write a program that reads an integer and prints the sum of its last 3 digits.
● Inputs ⇒ Outputs examples
○ 15 ⇒ 6
○ 125 ⇒ 8
○ 1000 ⇒ 0
○ 1001 ⇒ 1
○ 1234 ⇒ 9
○ 99999 ⇒ 27
'''
num = int(input())

digit1 = num % 10

num = num // 10

digit2 = num % 10

num = num // 10

digit3 = num % 10


print(digit1+digit2+digit3)
