n = int(input("Enter your width of v1 :"))
v1=[]
n2=int(input("Enter your width of v2 :"))
v2=[]

for i in range(n):
    x = int(input("Enter your value of v1 :"))
    v1.append(x)

for a in range(n2):
    x2 = int(input("Enter your value of v2 :"))
    v2.append(x2)

if v1==v2:
    print('perfect')
else:
    print('error')

print(v1,v2)