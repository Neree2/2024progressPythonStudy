sum=0
num1=0
while num1<=100:
    if num1 % 3 == 0 or num1 % 5 == 0:
        num1 += 1
        continue
    sum += num1
    num1 += 1
print(sum)