# MODULUS OPERATOR
# CHECKING EVEN OR NOT
checking_num = int(input("enter number to check for prime or not:"))
if checking_num % 2 == 0:
    print("yes its an even number!")
else:
    print("its not an even number!!")

# CHECKING WHETHER THE NUMBER IS POSITIVE , ZERO OR NEGATIVE

num = int(input("enter number to check?"))
if num > 0:
    print("its a positive number")
elif num == 0:
    print("oops its zero!!")
else:
    print("its a negative number")


# USER LOGIN
username = input("enter your username correctly ?")
password = input("enter your password for login?")
if username == 'world@24' and password == '1234567':
    print("login successfull")
else :
    print('invalid login details')

# CHECKING VOTING ELIGIBILITY
age = int(input("enter your age:"))
if age >= 18:
    print('congrats you are eligible!!')
else:
    print("oops you are not eligible!")

# MEMBERSHIP OPERATORS 
string = 'python programming'
print(' 'in string) 
print('pr' in string)
print('sp' not in string)
print('py' not in string)

# bitwise operators
a = 5
b = 3

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)

# SWAPPING NUMBERS USING OPERATORS
a = 100
b = 200
print("initial")
print(a)
print(b)

a = a + b
b = a - b
a = a - b
print("final")
print('a=',a)
print('b=',b)

# CHECKING THE USER INPUT YEAR IS WETHER LEAP YEAR OR NOT

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

    