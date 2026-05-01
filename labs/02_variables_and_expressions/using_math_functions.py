import math

x = float(input("Input x value: "))
y = float(input("Input y value: "))
z = float(input("Input z value: "))

test_1 = math.pow(x,z)
test_2 = math.pow(x,math.pow(y,z))
test_3 = math.fabs(x - y)
test_4 = math.sqrt (math.pow(x,z))

print(f"{test_1:.2f} {test_2:.2f} {test_3:.2f} {test_4:.2f}")
