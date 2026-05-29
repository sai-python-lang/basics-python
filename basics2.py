# BASICS OF DATA TYPES AND VARAIBLES

# AREA OF RECTANGLE 
c = int(input("enter length of the rectangle:"))
d = int(input("enter breadth of the rectangle:"))
print("area of the rectangle is :", c*d)

# CELSIUS TO FARENHEIT CONVERTOR
celsius = int(input("enter the celsius temperature to convert:"))
farenheit = (celsius * 9/5) + 32
print("farenheit reading is :",farenheit)

#  AVERAGE OF THREE NUMBERS
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))
print("average of three numbers is:", (num1+num2+num3)/3)

# CHECKING BOOLEAN VALUES
a = 10
b = 10
c = 50
print(a==b)
print(a==c)

# TYPE CASTING
X = "200"
Y = int(X)
print(Y + 50)

# FINDING SQUARE AND CUBE OF USER INPUT NUMBER
num = int(input("enter number rwquired:"))
print("square =",num **2)
print("cube =",num ** 3)

#  CALCULATING SIMPLE INTEREST
p = int(input("enter total amount to calculate:"))
t = int(input("enter time period for interest:"))
r = int(input("enter rate of interest for the amount:"))
simpleinterest = (p*t*r)/100
print("the simple interest is:",simpleinterest)


