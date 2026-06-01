print("Welcome to the Python ATM Machine Project!")
balance=1000
pin=9876
transaction_history=[]
for pinattempts in range(3):
    enter_pin=int(input("Please enter your 4-digit PIN:"))
    if enter_pin==pin:
        print("Login Successfull:")
        break
    else:
        print("Incorrect PIN. Try again.")

else:
    print("Too many attempts, account locked.")
    exit()

