print("****calculator****")
print("1.Adding")
print("2.subtracting")
print("3.multiply")
print("4.divide")
ch=int(input("enter the choice(1-4):"))
if ch==1:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    result=a+b
    print("result is:",result)
elif ch==2:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    result=a-b
    print("result is:",result)
elif ch==3:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    result=a*b
    print("result is:",result)
elif ch==4:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    result=a/b
    print("result is:",result)
else:
    print("envailid value")
    
