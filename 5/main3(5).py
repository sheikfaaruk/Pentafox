from datetime import date
a=input().split("-")
b=str(date.today()).split("-")
f_date=date(int(a[2]),int(a[1]),int(a[0]))
l_date=date(int(b[0]),int(b[1]),int(b[2]))
delta=l_date-f_date
print(delta.days)