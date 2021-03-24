import random
l=[]
A=int(input())
for i in range (A):
   n=random.sample(range(0,A),A)
   l.append(n)  
s=[]
for i in range(A):
    x=input('enter name')
    s.append(x)
for i in range(A):
    print("Day-",i+1,end=' ')
    for j in range(A):
        c=l[i][j]
        print(s[c],end=' ')
    print("\n")