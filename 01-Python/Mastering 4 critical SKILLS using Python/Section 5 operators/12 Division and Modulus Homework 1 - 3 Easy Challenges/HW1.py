'''
Homework 1: Averages
● Write a program that reads 5 numbers and print the following:
○ A) Their average
○ B) The sum of the first 3 numbers divided by the sum of the last 2 numbers
○ C) The average of the first 3 numbers divided by the average of the last 2 numbers.
○ What is the math relation between B and C?
● Input 1 2 3 4 5
○ 3
○ 0.666666667
○ 0.444444444
'''
num1 , num2 , num3 , num4 , num5 = map(int , input().split())

print( (num1+num2+num3+num4+num5) / 5.0)
print( (num1+num2+num3) / (num1+num2))
print( ((num1+num2+num3)/3.0) / ((num1+num2)/2.0))