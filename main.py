def Greeting():
    name = input("What is your name?\n")
    print("Hello, " + name)

def Age():
    age = int(input("How old are you?\n"))
    print(f"You will be {age + 1} years next year")

def Sum():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"Sum of {num1} and {num2} = {num1 - num2}")

def Area():
    length = float(input("Length = "))
    width = float(input("Width = "))
    print(f"Area = {length + width}")

tasks = {
    "1" : Greeting,
    "2" : Age,
    "3" : Sum,
    "4" : Area
}

while True:
    print("\n---Menu---")
    print("1 - Greeting")
    print("2 - Age")
    print("3 - Sum")
    print("4 - Area")
    print("0 - Exit")

    choise = input("Choose the function: ")

    if choise == "0":
        break

    elif choise in tasks:
        tasks[choise]()

    else:
        print("Wrong number")
