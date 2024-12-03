def enquiry():
    res=input("Are u want to continue the calculation:(yes/no) [case sensitive] ?")
    s1="yes"
    if res == s1: 
        pos_neg()
    else:
        print(".....THANK YOU .....")
        print("........BYE.........")
        exit()
def main():
    print()
    print("....Welcome to positive & negative number identifier....")
def pos_neg():
    num=float(input("Enter any number:"))
    if num > 0:
        print("{} is positive number.".format(num))
        enquiry()
    elif num == 0:
        print(f"{num} is Neutral number.")
        enquiry()
    else:
        print(f"{num} is Negative number.")
        enquiry()
main()
pos_neg()