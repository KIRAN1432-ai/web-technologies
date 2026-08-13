# l=[20,22,13,14,15,16]
# def my_map(func,value):
#     res=[]
#     for i in value:
#         value=func(i)
#         res.append(value)
#     return res
# print(list(map(lambda x:x*2,filter(lambda x:x%2==0,l))))
# print(list(my_map(lambda x: x*2 ,filter(lambda x:x%2==0,l))))
def fac(a):
    p=1
    for i in range(1,a):
        p+=p*i
    return p
print("---strong number---")
n=int(input())
t=n
s=0
while n>0:
    r=n%10
    s+=fac(r)
    n=n//10
if(s==t):
    print("strong number")
else:
    print("not strong number")

x=int(input())
print("----automorphic----")
l=len(str(x))
v=x**2
b=0
for i in range(l):
    r=v%10
    b=b*10+r
    v=v//10
s=0
while b>0:
    r=b%10
    s=s*10+r
    b=b//10
if(x==s):
    print("automorphic")
else:
    print("not automorphic")
z=int(input())
print("---spy---")
pr=1
suuu=0
while z>0:
    rx=z%10
    suuu+=rx
    pr*=rx
    z=z//10
if(suuu==pr):
    print("spy")
else:
    print("not spy")


i=int(input())
print("---perfect number--")
k=1
suu=0
while k<i:
    if(i%k==0):
        suu+=k
    k+=1
if (suu==i):
    print("perfect")
else:
    print("Not perfect")
print("----tech number---")
n1=int(input())
t2=n1
t=n1
c=0
while n1>0:
    re=n1%10
    c+=1
    n1=n1//10
#print(c)
if(c%2==0):
    su=0
    for i in range(c//2):
        ree=t%10
        su=su*10+ree
        t=t//10
    e=0
    while su>0:
        ru=su%10
        e=e*10+ru
        su=su//10
    tec=e+t
    if((tec)**2==t2):
        print("Techie")
