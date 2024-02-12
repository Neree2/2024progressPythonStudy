# มากสุดอันดับที่ 1 มากสุดอันดับ 2 น้อยสุดอันดับ 1 น้อยสุดอันดับ 2
n = int(input("Enter your width :"))
num = []
for i in range(n):
    x = int(input("Enter your value :"))
    num.append(x)
print(num)
count_odd =[]
for i in num:
    if i%2 !=0:
        count_odd.append(i)
print("Number of odd = ",count_odd,len(count_odd))
