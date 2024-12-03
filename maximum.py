def enquiry():
    res=input("Are u want to continue the calculation:(yes/no) [case sensitive] ?")
    s1="yes"
    if res == s1: 
        max()
    else:
        print(".....THANK YOU .....")
        print("........BYE.........")
        exit()
def main():
    print()
    print("....Welcome to maximum & minimum number identifier....")
def max():
    a=int(input("Enter value for a:"))
    b=int(input("Enter value for b:"))
    c=int(input("Enter value for c:"))
    if (a>b) and (a>c):
        print("{0} is maximum number among {1},{2},{3} numbers".format(a,a,b,c))
        print()
        enquiry()
    elif (b>a) and (b>c):
        print("{0} is maximum number among {1},{2},{3} numbers".format(b,a,b,c))
        print()
        enquiry()
    else:
        print("{0} is maximum number among {1},{2},{3} numbers".format(c,a,b,c))
        print()
        enquiry()
main()
max()
