try:
    no=int(input("\t Enter the number=>"))
    assert no>-1 and no<101,"INVALID NUMBER"
except AssertionError as ass:
    print("\t Error marks")
    print(ass)
