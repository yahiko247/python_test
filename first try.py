def Calculator():
    print("Simple calculator")
    print("1). Addition")
    print("2). Subtraction")
    print("3). Division")
    print("4). Multiplication")
    print("press 1 for addtion and press 2 for subtractio")

    chose = input("Chose 1, 2, 3, 4: ")

    if chose in ('1', '2', '3', '4'):
        num1 = float(input("enter number: "))
        num2 = float(input("enter number2: "))

        if chose == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        if chose =='2':
            print(f"{num1} - {num2} = {num1 - num2}")
        if chose == '3':
            print(f"{num1} / {num2} = {num1 / num2}")
        if chose == '4':
            print(f'{num1} * {num2} = {num1 * num2}')
    else:
        print("you entered wrong number")

#call the function
Calculator()