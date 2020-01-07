no=[]
for loop in range(0,10):
    value=int(input("\t No=>"))
    no.append(value)

def findodd(no):
    odd=[]
    for each in no:
        if each % 2 == 0:
            odd.append(each)
    return odd

def findmax(odd):
    val=odd[0]
    for each in odd:
        if val <= each:
            val = each
    return val

maxodd=findodd(no)
maxall=findmax(maxodd)
print("odd",maxall)

