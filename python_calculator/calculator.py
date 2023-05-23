print("Welcome to the calculator!")
while True:
    try:
        firstNum = int(input("Please enter the first number: "))
        operation = input("Please enter operation you'd like to perform (+, -, *, /, ^): ")
        secondNum = int(input("Please enter the second number: "))
        match operation:
            case '+':
                print(firstNum + secondNum)
            case '-':
                print(firstNum - secondNum)
            case '*':
                print(firstNum * secondNum)
            case '/':
                print(firstNum / secondNum)
            case '^':
                print(firstNum ^ secondNum)
            case _:
                print("Operation does not exist.")
    except:
        print("Incorrect input.")
