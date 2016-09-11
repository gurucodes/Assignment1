__author__ = 'GurdevSalhotra'
import csv
MENU = "Menu:\nR - List required items\nC - List completed items\nA - Add new item\nM - Mark an item as completed\nQ - Quit"
LISTARRAY = []

def main():
    loadItems()
    print("Shopping List 1.0 - by Gurdev Salhotra\n"+str(len(LISTARRAY))+" items loaded form items.CSV")
    menuChoice()

def menuChoice():
    print(MENU)
    choice = input(">>>")
    while(not choice or not(choice.isalpha())):
        print("Enter valid choice")
        menuChoice()
    if choice == "R" or choice =="r":
        printRequired()
        menuChoice()
    elif choice == "C" or choice =="c":
        printComplete()
        menuChoice()
    elif choice == "M" or choice =="m":
        markComplete()
        menuChoice()
    elif choice == "A" or choice =="a":
        addItem()
        menuChoice()
    elif choice == "Q" or choice =="q":
        print(str(len(LISTARRAY))+ "items saved to items.csv")
        writeCSV()
        print("Have a nice day :-)")
        exit(0)


def loadItems():
    with open('items.csv') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        for row in readcsv:
            LISTARRAY.append([row[0],row[1],row[2],row[3]])

def writeCSV():
    with open('items.csv', "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in LISTARRAY:
            writer.writerow([val])


def printRequired():
    totalPrice = 0.0
    count = 0
    for i in range(0,len(LISTARRAY)):
        if str(LISTARRAY[i][3]) == "r":
            print(str(count)+".\t"+str(LISTARRAY[i][0])+"\t\t\t"+"$\t"+str(LISTARRAY[i][1])+"\t"+str(LISTARRAY[i][2]))
            totalPrice += float(LISTARRAY[i][1])
            count += 1
    if(count == 0):
        print("No Required items Items")
    else:
        print("Total expected price for "+str(count)+" items: "+str(totalPrice))
    return count


def printComplete():
    totalPrice = 0.0
    count = 0
    for i in range(0,len(LISTARRAY)):
        if str(LISTARRAY[i][3])=="c":
            print(str(count)+".\t"+str(LISTARRAY[i][0])+"\t\t\t"+"$\t"+str(LISTARRAY[i][1])+"\t"+str(LISTARRAY[i][2]))
            totalPrice += float(LISTARRAY[i][1])
            count += 1
    if(count == 0):
        print("No Completed Items")
    else:
        print("Total expected price for "+str(count)+" items: "+str(totalPrice))


def markComplete():
    count=printRequired()
    counter=0
    itemNumber = int(input("Enter the number of an item to mark as completed"))
    if (itemNumber<0 or itemNumber>count):
        print("Enter correct item number")
    else:
        for i in range(0,len(LISTARRAY)):
            if str(LISTARRAY[i][3]) == "r":
                counter+=1
            if(count==counter):
                LISTARRAY[i][3]="c"
                print(str(LISTARRAY[i][0])+" marked as complete")



def addItem():
    itemName = input("Item Name: ")
    while(not itemName):
        print("Input cannot be blank")
        itemName = input("Item Name: ")
    price = input("Price: $")
    while(not (price.isdigit())):
        while(price<0):
            print("Invalid input; Enter a valid number")
            price = input("Price: $")
    priority = input("Priority: ")
    while(not (priority.isdigit())):
        print("Invalid input; Enter a valid number")
        priority = input("Priority: ")
    LISTARRAY.append([itemName,price,priority,"r"])






main()