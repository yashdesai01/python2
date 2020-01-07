t1=()
print(t1)

t2=(1,2,"three",4.5)
print(t2)

t3=(t2,"six",7,"eight",9.0)
print(t3)

##print(t2+t3)

print((t2+t3)[3])
i=0
while(i<len(t3)):
    print("loaction=>",i+1,"=",t3[i])
    i=i+1
    
t4=(5,8,9)
print("max From",t4,":",max(t4))
print("min From",t4,":",min(t4))
