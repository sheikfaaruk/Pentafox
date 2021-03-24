a=input()
i=0
b=[]
while(i<len(a)-1) :
    count=1
    while(a[i]==a[i+1]): 
        i+=1
        count+=1
        if(i+1==len(a)):
            break
    if(count==1):
        b.append(str(a[i]))
    else:
        b.append(str(a[i])+str(count))
    i+=1
if(a[-1]!=a[-2]):
    b.append(a[-1])
c="".join(i for i in b)
print(c)