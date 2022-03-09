import math
import operator
while(1):
    choice = input("Enter your choice ")
    if (choice == "sin" or choice== "cos" or choice == "tan" or choice == "sinh" or choice== "cosh" or choice == "tanh"):
        a = int(input("Enter angle in degree "))
        if (choice == "sin"):
            res=math.sin(a)
            print("Sin(",a,") is",res)
        elif (choice == "cos"):
            res=math.cos(a)
            print("cos(",a,") is",res)
        elif (choice == "tan"):
            res=math.tan(a)
            print("tan(",a,") is",res)
        elif (choice == "sinh"):
            res=math.sinh(a)
            print("Sinh(",a,") is",res)
        elif (choice == "cosh"):
            res=math.cosh(a)
            print("cosh(",a,") is",res)
        elif (choice == "tanh"):
            res=math.tanh(a)
            print("tanh(",a,") is",res)
    elif (choice == "+" or choice == "-" or choice == "*" or choice == "/" or choice == "pow" or choice =="//" or choice == "%"):
        n1 = int(input("Enter first Number "))
        n2 = int(input("Enter Second Number "))
        # choice=input("Enter your choice ")
        if (choice == "+"):
            res=n1+n2
            print("Sum of numbers :",res)
        elif(choice == "-"):
            res=n1-n2
            print("Difference of Numbers are : ",res)
        elif (choice == "*"):
            res=operator.mul(n1,n2)
            print("Product of the numbers : ", res)
        elif (choice == "/"):
            res=operator.truediv(n1,n2)
            print("Division of the numbers : ", res)
        elif (choice == "%"):
            res= operator.mod(n1,n2)
            print("Remainder of",n1,"divided by",n2,"is",res)
        elif (choice =="pow"):
            res=operator.pow(n1,n2)
            print(n1,"power",n2,"is",res)
        elif (choice == "//"):
            res=operator.floordiv(n1,n2)
            print("Quotient when",n1,"divides",n2,"is",res)
    else:
        print("!!Alert!! Wrong choice, Enter a valid choice")
    choice = input("want to continue Y/N: ?")
    if (choice == "N" or choice == "n"):
        break

