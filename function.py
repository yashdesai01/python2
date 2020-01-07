#no1=int(input("Enter the number"))


def add(no1,no2):
    return no1 + no2
def sub(no1=5,no2=3):
    return no1-no2
def sum_sub(no1,no2):
    a = no1 + no2
    b = no1 - no2
    return a,b;
n1=25
n2=20

ans=add(n1,n2)
print("pos: add ans=",ans)
#using keyword par

ans=add(n1 , no2 = n2)
print("key: add ans=",ans)

ans=sub()
print("sub",ans)

ad,sb = sum_sub(6,3)
print("add:",ad,"\t sub",sb)

allans = sum_sub(5,11)
print("add=",allans[0],"sub=",allans[1])
print("hello",end="")
