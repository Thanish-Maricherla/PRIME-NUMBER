num = int(input("Enter a number : "))
temp = False
for i in range(2,num):
    if (num%i)==0:
        temp = True
        break
if temp:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")