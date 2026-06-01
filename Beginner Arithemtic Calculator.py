operant1=input("Enter the first number: ")
operant2=input("Enter the second number: ")
result=0

sign=input("Enter the operation you want to perform (+, -, *, /): ")

try:
    operant=float(operant1)
    operant2=float(operant2)
    if sign=="+":
        result=operant+operant2
    elif sign=="-":
        result=operant-operant2
    elif sign=="*":
        result=operant*operant2
    elif sign=="/":
        result=operant/operant2
    else:
        print("Invalid Operation")

    print(result)
except:
    print("Invalid input, please enter a number.")