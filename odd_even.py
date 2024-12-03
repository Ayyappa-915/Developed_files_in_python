def enquiry():
    res=input("Are u want to continue the calculation:(yes/no) [case sensitive] ?")
    if res.lower()=="yes":
        odd_even()
    else:
        print(".....THANK YOU .....")
        print("........BYE.........")
        exit()
def main():
    print("....Welcome to odd & even number identifier....")
def odd_even():
    print("Enter any number:")
    num=int(input())
    if num%2 == 0:
        print(f"{num} is even number")
        enquiry()
    else:
        print("{} is odd number.".format(num))
        enquiry()
main()
odd_even()