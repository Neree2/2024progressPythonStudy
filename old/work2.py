# สุ่มตัวเลขจำนวนเต็ม n ตัว ระหว่าง 1-10 โดย n รับมาจาก user 
# เก็บไว้ในตัวแปล list l แล้วหาค่าที่ไม่ซ้ำกันใน list l และ นำไปเก็บไว้ใน list m
import random

n = int(input("The amount of number :"))
l=[]
m=[]

for i in range(n):
    ran= random.randint(1,10)
    l.append(ran)
    c= l.count(ran)
    if c ==1:
        m.append(ran)

print(l)
print(m)