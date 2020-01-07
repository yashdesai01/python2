aa={1:"Mon",2:"Tue",3:"Wes",4:"Thu",5:"fri",6:"sat",7:"sun"}
value=int(input("Enter day choise=>"))
if(int(value) in aa):
    print(aa)
    day = aa(int(value))
    print("=",day)
else:
    print("Invalid")
