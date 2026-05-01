num1 = int(input())
num2 = int(input())
num3 = int(input())

smallest = num1
if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3

print(smallest)