from car import Car
# List of cars in the system
inventory = []

def menu():
    print("\n")
    print("*** Welcome to DealerX system ***")
    print("-"*33)
    print("1 - Register a new Car")
    print("2 - See Inventory Items")
    print("3 - Count by Year")
    print("X - Exit the System")
    print("\n")
    opc = input("Please choose an option ")
    return opc

def count_year():
    count = 0
    y = int(input("What year of car are you looking for? I can tell you how many we have in that year. "))
    for i in inventory:
        print(i.year)
        if i.year == y:
            count +=1
    print("We have "+str(count))

# Logic to ask the user for the car info
# Create a car object
# Add the car to a list
def create_new():
    print("The user wants to create X")
    try:
        make = input("What is the make? ")
        year = int(input("What is the year? "))
        cyls = int(input("How many cylinders? "))
        color = input("What is the color? ")
        price = float(input("What is the price? "))
        v = Car(make,year,cyls,color,price)
        inventory.append(v)
        input("Car Created. Press Enter to continue")
    except:
        # something crashed above
        print("*** Your data is not valid ****")
    
def print_list():
    #travel the array for each car, print its info
    for i in inventory:
        i.print_info()

# Start the system
selection=""
while selection != "x":
    selection = menu()

    if(selection == "1"):
        create_new()
    elif(selection == "2"):
        print_list()
    elif(selection == "3"):
        count_year()

    
