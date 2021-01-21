#letsupgrade day 3 Assignment Question - 2
a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

def swap(a,b):
    a,b=b,a
    return a,b

a,b=swap(a,b)

print("The values after swapping is : ",a,b)

