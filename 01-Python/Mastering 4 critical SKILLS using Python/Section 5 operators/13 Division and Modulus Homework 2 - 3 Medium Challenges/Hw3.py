'''
Homework 3: 4th digits from the end
● Write a program that reads an integer and print the 4th from the right side. If 
no such digit, print 0
● Inputs => outputs
○ 15 => 0
○ 125 => 0
○ 1000 => 1
○ 5001 => 5
○ 1234 => 1
○ 654321 => 4
○ 99999 => 9
'''

num = int(input())

digit4 = (num % 10000) // 1000

print(digit4)

