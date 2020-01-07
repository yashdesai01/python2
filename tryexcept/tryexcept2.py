try:
    no1=int(input("\t Enter the No1=>"))
    no2=int(input("\t Enter the No2=>"))
    div=no1/no2
    print(div)
except ZeroDivisionError as Zde:
    print(Zde)
except ValueError as Ve:
    print(Ve)
except NameError as Ne:
    print(Ne)
except Exception as Ex:
    print(Ex)
except Exception:
    print("\t Error")
else:
    print("\t Done succesfully")
