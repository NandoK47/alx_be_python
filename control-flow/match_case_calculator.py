num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case"+":
        print("The result is, {sum}")
    case"-":
        print("The result is, {difference}")
    case"*":
        print("The result is, {product}")
    case"/":
        if num2 > 0:
            print("The result is, {division}")
        else:
            num2 !=0
            print("cannot divide by zero")
