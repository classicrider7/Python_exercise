import math
import operator
"""Infinte loop"""
while(1):
    """ creating user defined function """
    def add(a,b):
        """ User defined function for addition/ summation. We will get inputs from user """
        res=operator.add(a,b)
        """ function body and storing output in result as res """
        return res
    def diff(a,b):
        """ User defined function for subtraction. We will get inputs from user """
        res=n1-n2
        return res
    def mul(a,b):
        """ User defined function for Multiplication. We will get inputs from user """
        res=operator.mul(n1,n2)
        return res
    def div(a,b):
        """ User defined function for division. We will get inputs from user """
        res=operator.truediv(n1,n2)
        return res
    def mod(a,b):
        """ User defined function for finding modulas. We will get inputs from user """
        res= operator.mod(n1,n2)
        return res
    def pow(a,b):
        """ User defined function for finding power, i.e A power B or A^B or A**B. We will get inputs from user """
        res=operator.pow(n1,n2)
        return res
    def floordiv(a,b):
        """ User defined function for floordiv test. We will get inputs from user """
        res=operator.floordiv(n1,n2)
        return res
    def sin(q):
        res=math.sin(q)
        return res
    def cos(q):
        res= math.cos(q)
        return res
    def tan(q):
        res= math.tan(q)
        return res
    def cosh(q):
        res= math.cosh(q)
        return res
    def sinh(q):
        res= math.sinh(q)
        return res
    def tanh(q):
        res= math.tanh(q)
        return res

    choice = input("Enter your choice ")
    if (choice == "sin" or choice== "cos" or choice == "tan" or choice == "sinh" or choice== "cosh" or choice == "tanh"):
        a = int(input("Enter angle in degree "))
        if (choice == "sin"):
            s=sin(a)
            print("Sin(",a,") is",s)
        elif (choice == "cos"):
            s=cos(a)
            print("cos(",a,") is",s)
        elif (choice == "tan"):
            s=tan(a)
            print("tan(",a,") is",s)
        elif (choice == "sinh"):
            s=sinh(a)
            print("Sinh(",a,") is",s)
        elif (choice == "cosh"):
            s=cosh(a)
            print("cosh(",a,") is",s)
        elif (choice == "tanh"):
            s=tanh(a)
            print("tanh(",a,") is",s)
    elif (choice == "+" or choice == "-" or choice == "*" or choice == "/" or choice == "pow" or choice =="//" or choice == "%"):
        n1 = int(input("enter first number "))
        n2 = int(input("enter second number "))
        if (choice == "+"):
            s=add(n1,n2)
            print("summation of Numbers are : ",s)
        elif (choice =="-"):
            s=diff(n1,n2)
            print("Difference of Numbers are : ",s)
        elif (choice == "*"):
            s=mul(n1,n2)
            print("Product of the numbers : ", s)
        elif (choice == "/"):
            s=div(n1,n2)
            print("Division of the numbers : ", s)
        elif (choice == "%"):
            s=mod(n1,n2)
            print("Remainder of", n1, "divided by", n2, "is", s)
        elif (choice == "pow"):
            s=pow(n1,n2)
            print(n1, "power", n2, "is", s)
        elif (choice == "//"):
            s=floordiv(n1,n2)
            print("Quotient when",n1,"divides",n2,"is",s)
    else:
        print("!!Alert!! Wrong choice, Enter a valid choice")
    choice = input("want to continue Y/N: ?")
    if (choice == "N" or choice == "n"):
        break
