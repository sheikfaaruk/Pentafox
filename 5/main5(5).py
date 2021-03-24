a=["test","name",45,"anything",True,78,45.5]
b={}
string=[]
number=[]
boolean=[]
floats=[]
for i in a:
    if(type(i) is str):
        string.append(i)
    elif(type(i) is bool):
        boolean.append(i)
    elif(type(i) is int):
        number.append(i)
    elif(type(i) is float):
        floats.append(i)
b["strings"]=string
b["numbers"]=number
b["booleans"]=boolean 
b["floats"]=floats
print(b)