# Import modules
from tabulate import tabulate
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return self.country + " " + self.code + " " + self.product + " " +self.cost+ " " + self.quantity

    # Method to return details of a shoe object as a list.
    def get_details_list(self):
        return [self.country, self.code, self.product, self.cost, self.quantity]


#=============Shoe list===========
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    try:
        with open("inventory.txt","r")as file:
            lines = file.readlines()
            
            # Using this line of code to exclude the first line.
            for indx in range(1,len(lines)):
                
                temp = lines[indx].strip()
                temp = temp.split(",")
         
                shoe_list.append(Shoe(temp[0], temp[1], temp[2], temp[3], temp[4]))
    except FileNotFoundError:
        print("The file does not exist")
        

def capture_shoes():
    # User enters data to append a new object into the shoe_list.
    # If the user enters inccorect data they will be asked to enter it again.
    while True:
        try:
            country = input("The country : ")
            code = input("Shoe code : ")
            product = input("Product name : ")
            cost = int(input("Shoe cost : "))
            quantity = int(input("Shoe quantity : "))

            shoe = (Shoe(country, code, product, str(cost), str(quantity)))
            shoe_list.append(shoe)
            read_shoes_data()
        
            with open("inventory.txt","a+") as file:
                temp = ((shoe).get_details_list())
                string = ",".join(temp)
                file.write(string + "\n")
            print("Shoe has been successfully captured\n")
            break
        except ValueError:
            print("Please enter the correct data")

def view_all():
    all_shoes = []
    head = ["Country", "Code", "Product", "Cost", "Quantity"]
    for indx in range(len((shoe_list))):        

        temp_list = shoe_list[indx].get_details_list()
        all_shoes.append(temp_list)

    # Each object is put in a grid using tabulate. 
    print(tabulate(all_shoes, headers=head, tablefmt="fancy_grid"))

def re_stock():
    # Adding all the quantities in a list.
    shoe_quantity = []
    for indx in range(1,len(shoe_list)):
        temp = (shoe_list[indx].quantity)
        shoe_quantity.append(int(temp))

    # Finding the lowest quantity and printing it out as a string.
    low = (min(shoe_quantity))
    index = (shoe_quantity.index(low))
    shoe = (shoe_list[index+1].__str__())
    print("The shoe that needs to be re-stocked : ")
    print(shoe, "\n")

    while True:
        check = input("Are you sure you want to update the quantity! (y/n) :").lower()

        if check == "y":
            new_quantity = []
            user_quantity = (input("Enter updated quantity : "))
            print("Item has been re-stocked successfully\n")

            # Open the file and write every shoe with the new updated quantity.
            with open("inventory.txt","r")as file:
                    lines = file.readlines()
        
                    for indx in range(len(lines)):
                        
                        temp = lines[indx].strip()               
                        temp = temp.split(",")
                        new_quantity.append(temp)
            
            new_quantity[index+2][4] = user_quantity

            # File gets ovewriten with new data.
            with open("inventory.txt","w")as file:
                for sub in new_quantity:
                    string = ",".join(sub)
                    file.write(string + "\n")

            file.close
            break

        elif check == "n":
            print("Shoe quantity has not been updated\n")

        else:
            print(f"{check} is incorrect! Please try again...\n")
        

def seach_shoe():
    # Shoe codes get appended into the list where the index can then be found for the object that needs to be displayed.
    shoe_search = []
    for indx in range(1,len(shoe_list)):
        temp = (shoe_list[indx].code)
        shoe_search.append(temp)

    # User enters the shoe code for the shoe they are looking for and prints out its string representaion.
    shoe_code = (input("Enter the shoe code for the shoe you are looking for \nEnter code here : "))
    print("The shoe you requested :")
    for count,indx in enumerate(shoe_search):
        if indx == shoe_code:
            print(shoe_list[count+1].__str__()+"\n")
            break

def value_per_item():
    print("Value of each shoe listed below:\n")
    # This function takes each objects cost and quantity attribute and multiplies it to get a value for each shoe object.
    for indx in range(1,len((shoe_list))):      
        shoe = (shoe_list[indx].__str__())  
        cost = int(shoe_list[indx].cost)
        quantity = int(shoe_list[indx].quantity)

        value = cost*quantity

        print(shoe, "\nValue = R", value, "\n")

def highest_qty():
    # Gets the highest quantity using max and prints out a string representation of the object with the highest quantity.
    shoe_quantity = []
    for indx in range(1,len(shoe_list)):
        temp = (shoe_list[indx].quantity)
        shoe_quantity.append(int(temp))

    maximum = (max(shoe_quantity))
    index = (shoe_quantity.index(maximum))
    print("This shoe is for sale :")
    shoe = (shoe_list[index+1].__str__())
    print(shoe + "\n")

#==========Main Menu=============
print("\t\t\tShoe Invetory\n")
read_shoes_data()
while True:
    try:
        inventory_menu = int(input('''Enter one of the following Options below:
            1 - Capture a new shoe
            2 - View all of the shoes
            3 - Re-stock shoe
            4 - Search for a shoe
            5 - Get the value of all shoes
            6 - Check which shoe should go on sale
            7 - Exit the program
            : '''))

        if inventory_menu == 1:
            capture_shoes()

        elif inventory_menu == 2:
            view_all()

        elif inventory_menu == 3:
            re_stock()

        elif inventory_menu == 4:
            seach_shoe()

        elif inventory_menu == 5:
            value_per_item()

        elif inventory_menu == 6:
            highest_qty()

        elif inventory_menu == 7:
            print('Goodbye!')
            break

        else:
            print("\nYou have made a wrong choice, Please Try again\n")
            
    except ValueError:
        print("\nEnter a valid option.Try again please...\n")

