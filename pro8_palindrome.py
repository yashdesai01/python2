def pal(no):
    val=0
    while(no>0):
        val=( val * 10 ) + ( no % 10 )
        no=no//10
    return val
    
no=int(input("Enter the number=>"))
if(no==pal(no)):
    print(no,"is palindrome")
else:
    print(no,"is not palindrome")

