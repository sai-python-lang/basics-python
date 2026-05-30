# CONDITIONAL STATEMENTS

# checking wether the number is divisible by {{5}}:########
num = int(input("enter the number to check:"))

if num % 5 == 0:
    # modulus  operator  gives  remainder  for  division

    print("yes its divisible by 5!!")
else:
    print("oops its not divisible by 5")

# checking character for vowel or consonant:#########
char = input("enter any character to check and verify:")

if char.lower() in "aeiou":
    # .lower() function changes every character to lowercase and checks for verification

    print("its a vowel")
else:
    print("its a consonant")

# DISCOUNT ELIGIBILITY ###

total_amount = int(input("enter total bill of shooping for verifying eligible discount??"))

if total_amount == 1000:
    print("hurray you are eligible for discount of 15% Off")
elif total_amount > 1000:
    print("awesome amount !!! you are eligible for 50% Off discount and bumper prizes ::")
else:
    print("NO DISCOUNT")

#  VOTING ELIGIBILITY ANS SENIOR ELIGIBILITY ######

age = int(input("enter your age for checking eligibility:?"))

if age >= 18:
    print("you are eligibile ::::")

    if age >= 60:
        # this statement follows only when age >= 18 becomes true
        print("you are a senior citizen!!")
else:
    print("not eligible for voting")

# ATM WITHDRAWAL

balance = 5000
amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    # first it verifies the amount is less than the balance amount 
    if amount % 100 == 0:
        print("Transaction Successful")
        # the amount should be multiple of 100 ,then transaction follow up
    else:
        print("Amount should be multiple of 100")
else:
    # thus statement follows only when amount is >>> balance
    print("Insufficient Balance")








