__author__ = 'Gurdev'

def get_number(lower,upper):
    number = input("Enter a number ({}-{}): ".format(lower, upper))
    while(number.isalpha()):
        print("Invalid input please try again")
        number = input("Enter a number ({}-{}): ".format(lower, upper))

    while(int(number)<lower or int(number)>upper):
        print("Invalid input please try again")
        number = input("Enter a number ({}-{}): ".format(lower, upper))
def main():
    lower = 10
    upper = 100
    number = get_number(lower,upper)
    print(chr(int(number)))

main()