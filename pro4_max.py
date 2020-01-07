def max1(no1,no2,no3):
##    return (no1>no2)?(no1>no3)?no1:no3:(no2>no3)?no2:no3
    if no1>no2 and no1>no3:
        print("\t No1 is max=>",no1)
    elif no2>no1 and no2>no3:
        print("\t No2 is max=>",no2)
    else:
        print("\t No3 is max",no3)
    return no1,no2,no3;

no1=int(input("\t Enter the no1=>"))
no2=int(input("\t Enter the no2=>"))
no3=int(input("\t Enter the no3=>"))
max1(no1,no2,no3)
##print("max=>",ans)
