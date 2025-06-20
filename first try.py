print("Simple calculator/n")
print("press 1 for addtion and press 2 for subtractio")

chose = input("Chose 1 or 2: ")

if chose in ('1', '2'):
    num1 = float(input("enter number: "))
    num2 = float(input("enter number2: "))

    if chose == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    if chose =='2':
        print(f"{num1} - {num2} = {num1 - num2}")
