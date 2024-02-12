giveme=str(input('enter word: '))
list2=[]
count=0
for i in giveme:
    list2.append(i)
for j in list2:
    if j=='a':
        count+=1
    elif j=='e':
        count+=1
    elif j=='i':
        count+=1
    elif j=='o':
        count+=1
    elif j=='u':
        count+=1

print(count)