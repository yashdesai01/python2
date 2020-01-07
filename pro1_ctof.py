def cf(cel):
    return cel * 1.8 + 32
    
def fc(fah):
    return (fah1 -32) / 1.8
    
while(True):
    print("\t1. Celsius to fahrenheit")
    print("\t2. fahrenheit to Celsius")
    print("\t3. Exit")
    ch=int(input("\t Enter the selection=>"))
    if(ch>=3):
        print("bye")
        break
    if(ch==1):
        cel=float(input("\t Enetr the celsius=>"))
        fah = cf(cel)
        print("\t fahrenhit=>",fah)
        print("\t%.2f degree celsius is equal to %.2f degree fahrenheit"%(cel,fah))

    elif(ch==2):
        fah=float(input("\t Enter the fahrenhit=>"))
        cel = fc(fah)
        print("\t celsius=>",cel)
        print("\t%.2f degree fahrenheit is equal to %.2f degree celsius"%(fah,cel))

    else:
        print("wrong choise")
    continue


    
