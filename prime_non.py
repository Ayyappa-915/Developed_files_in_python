def enquiry():
    res=input("Are u want to continue the calculation:(yes/no) [case sensitive] ?")
    s1="yes"
    if res == s1: 
        prime_non()
    else:
        print(".....THANK YOU .....")
        print("........BYE.........")
        exit()
def main():
    print()
    print("**** Welcome to prime or non-prime number identifier ****")
def prime_non():
    num=int(input("Enter any number:"))
    count=0
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                count=1
                break
        if count == 0:
            print(f"{num} is prime number")
            print()
            enquiry()
        else:
            print(f"{num} is not a prime number.")
            print()
            enquiry()
    elif num == 1 or num == 0:
        print(f'{num} is a not a prime number.')
        print()
        enquiry()
    else:
        print("negative numbers are not prime numbers.")
        print()
        enquiry()
main()
prime_non()
        
