array=[]
sum=0
size=int(input("Enter how many numbers are you want to add:"))
print("Enter {} numbers".format(size))
for i in range(size):
    array.append(int(input()))
    sum+=array[i]
print("The numbers you are entered are:")
for i in range(len(array)):
    print(array[i],end="  ")
print("\nsum of given elements is:{}".format(sum))

