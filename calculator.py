def add(no1,no2):
    return no1 + no2
    
def sub(no1,no2):
    return no1 - no2

def mul(no1,no2):
    return no1 * no2

def div(no1,no2):
    return no1 / no2

def mod(no1,no2):
    return no1 % no2
    
while(True):
    print("\t1. Add")
    print("\t2. sub")
    print("\t3. mul")
    print("\t4. div")
    print("\t5. mod")
    ch=int(input("\t Enetr the selection=>"))
    if(ch>=6):
        print("bye")
        break
    if(ch==1):
        no1=int(input("\t Enetr the no1=>"))
        no2=int(input("\t Enetr the no2=>"))
        ans = add(no1,no2)
        print("\t add=>",ans)
        
    elif(ch==2):
        no1=int(input("\t Enetr the no1=>"))
        no2=int(input("\t Enetr the no2=>"))
        ans = sub(no1,no2)
        print("\t sub=>",ans)

    elif(ch==3):
        no1=int(input("\t Enetr the no1=>"))
        no2=int(input("\t Enetr the no2=>"))
        ans = mul(no1,no2)
        print("\t mul=>",ans)
    
    elif(ch==4):
        no1=int(input("\t Enetr the no1=>"))
        no2=int(input("\t Enetr the no2=>"))
        ans = div(no1,no2)
        print("\t mul=>",ans)
        
    elif(ch==5):
        no1=int(input("\t Enetr the no1=>"))
        no2=int(input("\t Enetr the no2=>"))
        ans = mod(no1,no2)
        print("\t module=>",ans)
    
    else:
        print("wrong choise")
    continue


    
