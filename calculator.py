def add(a,b):
    c=a+b
    print("sum of given numbers=", c)
def sub(a,b):
    c=a-b
    print("difference of given numbers=",  c)
def mul(a,b):
    c=a*b
    print("multiplication of given numbers=",  c)
def div(a,b):
    c=a/b
    print("true division is=",  c)
def fdiv(a,b):
    c=a//b
    print("quotient is=",  c)
def mdiv(a,b):
    c=a%b
    print("remainder is=", c)
def enquiry():
    res=input("Are u want to continue the calculation:(yes/no) [case sensitive] ?")
    s1="yes"
    if res == s1: 
        calculator()
    else:
        print(".....THANK YOU .....")
        print("........BYE.........")
        exit()
def main():
    print()
    print("*** WELCOME TO ARITHMETIC CALCULATOR ***")
def calculator():
    print()
    print("1.ADDITION")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.TRUE DIVISION")
    print("5.FLOOR DIVISION")
    print("6.MODULO DIVISION")
    print()
    choice=int(input("select the option do you want to perform :  ")) 
    if choice == 1:
        a=int(input("enter the value for a:"))
        b=int(input("Enter the value for b:"))
        add(a,b)
        enquiry()
    elif choice == 2:
        a=int(input("enter the value for a:"))
        b=int(input("Enter the value for b:"))
        sub(a,b)
        enquiry()
    elif choice==3:
        a=int(input("enter the value for a:"))
        b=int(input("Enter the value for b:"))
        mul(a,b)
        enquiry()
    elif choice==4:
        a=int(input("enter the value for a:"))
        b=int(input("Enter the value for b:"))
        div(a,b)
        enquiry()
    elif choice==5:
        a=int(input("enter the value for a:"))
        b=int(input("Enter the value for b:"))
        fdiv(a,b)
        enquiry()
    elif choice==6:
        a=int(input("enter the value for a:"))
        b=int(input("Enter the value for b:"))
        mdiv(a,b)
        enquiry()
    else:
        print(".....Invalid option.please choose valid option......")
        print()
        enquiry()
main()
calculator()
