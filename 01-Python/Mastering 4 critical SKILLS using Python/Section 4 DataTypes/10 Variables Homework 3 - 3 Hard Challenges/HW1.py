num1,num2,num3 = map(int , input().split())

temp = num2
num2 = num3
num3 = num1
num1 = temp

print(num1 , num2 , num3)