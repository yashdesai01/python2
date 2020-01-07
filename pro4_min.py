def max1(no1,no2,no3):
##    return (no1>no2)?(no1>no3)?no1:no3:(no2>no3)?no2:no3
    if no1<no2 and no1<no3:
        print("\t No1 is min=>",no1)
    elif no2<no1 and no2<no3:
        print("\t No2 is min=>",no2)
    else:
        print("\t No3 is min",no3)
    return no1,no2,no3;

no1=int(input("\t Enter the no1=>"))
no2=int(input("\t Enter the no2=>"))
no3=int(input("\t Enter the no3=>"))
max1(no1,no2,no3)
##print("max=>",ans)
