n= int(input("time used for run:"))


if n>=86400:
    print(n//86400)
    n=n%86400
else:
    print(0)
if n>=3600:
    print(n//3600)
    n=n%3600
else:
    print(0)
if n>=60:
    print(n//60)
    n=n%60
else:
    print(0)
if n>=1:
    print(n//1)
    n=n%18
else:
    print(0)