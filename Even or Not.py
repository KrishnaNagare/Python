#2. Apply if-else condition to check whether number is even or not
a = int(input("Enter a number: "))
if a == 0:
    print(a, "is equal to 0")
elif a % 2 == 0:
    print(a, "is an even number")
else:
    print(a, "is an odd number")
