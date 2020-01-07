no=input("\t Enter no")
pow1=len(no)
sum1=0
temp=int(no)

while temp!=0:
    rem = temp % 10
    sum1 = sum1 + rem ** pow1
    temp = temp // 10

if sum1==int(no):
    print(sum1,"is armstrong")
else:
    print(sum1,"is not armstrong")

