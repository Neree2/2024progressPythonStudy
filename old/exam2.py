t=int(input("tinki's income: "))
d=int(input("dizzy's income: "))
l=int(input("lala's income: "))
p=int(input("pole's income: "))

if t<100000:
    tt=0
if 500000>=t>=100000:
    tt= ((t*5)/100)
if 500001>=t>=1000000:
    tt= ((t*10)/100)
if t> 1000000:
    dt= ((d*20)/100)
if d<100000:
    dt=0
if 500000>=d>=100000:
    dt= ((d*5)/100)
if 500001>=d>=1000000:
    dt= ((d*10)/100)
if d>1000000:
    dt= ((d*20)/100)
if l<100000:
    lt=0
if 500000>=l>=100000:
    lt= ((l*5)/100)
if 500001>=l>=1000000:
    lt= ((l*10)/100)
if l> 1000000:
    lt= ((l*20)/100)
if p<100000:
    pt=0
if 500000>=p>=100000:
    pt= ((p*5)/100)
if 500001>=p>=1000000:
    pt= ((p*10)/100)
if p> 1000000:
    pt= ((p*20)/100)

print(t)
print(d)
print(l)
print(p)
print(float(tt+dt+lt+pt))