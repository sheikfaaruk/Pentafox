a=input()
b=input()
c=[]
for i in a:
    if i not in b:
        c.append(i)
for i in b:
    if i not in a:
        c.append(i)
d="".join(i for i in c)
print(d)