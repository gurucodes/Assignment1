__author__ = 'Gurdev'
def main():
    numItems = int(input("Number of items: "))
    while(numItems<=0):
        print("Invalid number of items")
        numItems = int(input("Number of items: "))
    total = 0
    for i in range(0,numItems,1):
        price = float(input("Price of item: "))
        total = total+price
    if total>100:
        total = total - (total*0.1)
    print("Total price for"+str(numItems)+"items is" + str(total))



main()