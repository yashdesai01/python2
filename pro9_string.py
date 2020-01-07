## Write a Python program to perform following operation on given string input: 
## a) Count Number of Vowel in given string
## b) Count Length of string (donot use len() )
## c) Reverse string
## d) Find and replace operation
## e) check whether string entered is a palindrome or not 

print("Enter your choise")
print("1. Count Number of Vowel in given string")
print("2. Count Length of string (donot use len())")
print("3. Reverse string")
print("4. Find and replace operation")
print("5. check whether string entered is a palindrome or not\n")
sel=int(input("Enter your choise=>"))

def strval(valstr):
    total=0
    for each in valstr:
        if(each=="a" or each=="e" or each=="i" or each=="o" or each=="u"):
            total = total + 1
    return total

def lenstr(valstr):
    total=0
    for each in valstr:
        total = total + 1
    return total

def revstr(valstr):
    return valstr[::-1]
        
##def findstr(valstr):
##    while(valstr>0)    
if(sel==1):
    valstr=input("Enter the string=>")
    print("Number of Vowel string=>",strval(valstr))
elif(sel == 2):
    valstr=input("Enter the string=>")
    print("length of string=>",lenstr(valstr))
elif(sel == 3):
    valstr=input("Enter the string=>")
    print("Reverse string=>",revstr(valstr))
elif(sel == 4):
    valstr=input("Enter the string=>")
    print("Reverse string=>",findstr(valstr))
else:
    print("invalid")
