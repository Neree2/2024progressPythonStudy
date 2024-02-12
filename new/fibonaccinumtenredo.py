num1 = 1
num2 = 0

while num2 < 55:
    num2 += num1
    if num2 >= 55:
        print(num1, num2)
    else:
        print(num1, num2, end=' ')
    num1 += num2
