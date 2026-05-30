#  In Python, loops are used to execute a block of code repeatedly until a condition is met or all items in a sequence are processed.

# ----- FOR LOOP -----
# RIGHT ANGLED STAR PROGRAM :

rows = 6
# we can decide how many rows we ne this type pattern other wise it runs over infinity 

for i in range(1 , rows+1):
    # for loop considers starting point and ending point -1 
    print("^" * i)

# FLOYD'S TRIANGLE:

rows = 5
num = 1
for i in range(1 , rows+1):
    for j in range(i):
        print(num,end = ' ')
        num += 1
    print()

# FIBONACCI SERIES:
n = int(input("enter no.of terms required in your series?"))
a = 0
b = 1 
for i in range(n):
    print(a , end =" ")
    c = a+b
    a = b
    b = c

# PRIME NUMBER CHECK
num = int(input("Enter a number: "))

if num < 2:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
    
# FACTORIAL OF USER INPUT NUMBER
num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)

