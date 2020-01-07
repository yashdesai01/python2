try:
    no1=int(input("\t Enter the No1=>"))
    no2=int(input("\t Enter the No2=>"))
    div=no1/no2
    print(div)
except ZeroDivisionError:
    print("Divide by zero")
except ValueError:
    print("Invalid data for performming divison operation")
except NameError:
    print("\t plz initialzed value")
except Exception:
    print("\t Error")
else:
    print("\t Done succesfully")
