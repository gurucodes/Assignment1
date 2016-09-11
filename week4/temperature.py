__author__ = 'Gurdev'


def farToCel():
    fahrenheit = float(input("Farenhiet: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result: {:.2f} F".format(celsius))

def celToFar():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celToFar()
    elif choice == "F":
        farToCel()
        pass
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")