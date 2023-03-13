# import library
import csv
import datetime

# Create a text file and write the menu options to a text file
file = open("Menu.txt", "w")
file.write("* Please Choose a Pizza Base:\n")
file.write("1: Classic\n")
file.write("2: Margherita\n")
file.write("3: TurkPizza\n")
file.write("4: PlainPizza\n")
file.write("5: Vegetarian\n")
file.write("6: Neapolitan\n")
file.write("7: Hawaiian\n")
file.write("8: Mexican\n")
file.write("9: Chicago\n")
file.write("10: Greek\n")
file.write("* and sauce of your choice:\n")
file.write("1: Olives\n")
file.write("2: Mushrooms\n")
file.write("3: GoatCheese\n")
file.write("4: Meat\n")
file.write("5: Onions\n")
file.write("6: Corn\n")
file.write("* Thank you!\n")
file.close()


# Create a Pizza superclass
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    # Defining methods for encapsulation
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


# Create Pizza subclasses for different types of pizza
class Classic(Pizza):
    def __init__(self):
        super().__init__("Tomato sauce, pepperoni and cheese", 85.99)


class Margherita(Pizza):
    def __init__(self):
        super().__init__("Tomato sauce, mozzarella cheese and basil leaves", 90.99)


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Tomato sauce, pepperoni, green peppers, onions and cheese", 100.99)


class PlainPizza(Pizza):
    def __init__(self):
        super().__init__("Tomato sauce and mozzarella cheese", 80.99)


class Vegetarian(Pizza):
    def __init__(self):
        super().__init__("Tomato sauce, mushrooms, green peppers, tomatoes, onions and black olives", 100.99)


class Neapolitan(Pizza):
    def __init__(self):
        super().__init__("San Marzano tomato sauce, tomatoes, basil leaves, oregano and mozzarella cheese", 100.99)


class Hawaiian(Pizza):
    def __init__(self):
        super().__init__("Tomato sauce, ham, pineapple and mozzarella cheese", 110.99)


class Mexican(Pizza):
    def __init__(self):
        super().__init__("Tortillas, enchilada sauce, tomatoes, black beans, scallions, Mexican cheese blend", 110.99)


class Chicago(Pizza):
    def __init__(self):
        super().__init__("Crispy deep-dish crust, tomato sauce and cheese", 90.99)


class Greek(Pizza):
    def __init__(self):
        super().__init__("Tomato sauce, tomatoes, kalamata olives, oregano, feta cheese and mozzarella cheese", 100.99)


# Define decorator class that uses methods and arguments in pizza class
class Decorator(Pizza):
    def __init__(self, component, description, cost):
        self.component = component
        super().__init__(description, cost)

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)


class Olives(Decorator):
    def __init__(self, component):
        super().__init__(component, "Olives", 2.00)


class Mushrooms(Decorator):
    def __init__(self, component):
        super().__init__(component, "Mushrooms", 3.00)


class GoatCheese(Decorator):
    def __init__(self, component):
        super().__init__(component, "Goat Cheese", 5.00)


class Meat(Decorator):
    def __init__(self, component):
        super().__init__(component, "Meat", 10.00)


class Onions(Decorator):
    def __init__(self, component):
        super().__init__(component, "Onion", 4.00)


class Corn(Decorator):
    def __init__(self, component):
        super().__init__(component, "Corn", 2.00)


def main():
    # Open the menu file in read mode and print it to the console
    f = open("Menu.txt", "r")
    print(f.read())
    # Prompt the user to select a pizza base
    pizza_choice = int(input("Please select the pizza base: "))
    pizza = None
    # Validate the user input for the pizza base and create the pizza object accordingly
    while pizza_choice < 1 or pizza_choice > 10:
        print("Invalid choice, try again.")
        pizza_choice = int(input("Please select the pizza base: "))

    if pizza_choice == 1:
        pizza = Classic()
    elif pizza_choice == 2:
        pizza = Margherita()
    elif pizza_choice == 3:
        pizza = TurkPizza()
    elif pizza_choice == 4:
        pizza = PlainPizza()
    elif pizza_choice == 5:
        pizza = Vegetarian()
    elif pizza_choice == 6:
        pizza = Neapolitan()
    elif pizza_choice == 7:
        pizza = Hawaiian()
    elif pizza_choice == 8:
        pizza = Mexican()
    elif pizza_choice == 9:
        pizza = Chicago()
    elif pizza_choice == 10:
        pizza = Greek()

    # Prompt the user to select a sauce
    sauce_choice = int(input("Please select sauce: "))

    # Validate the user input for the sauce and add it to the pizza object
    while sauce_choice < 1 or sauce_choice > 6:
        print("Invalid choice, try again.")
        sauce_choice = int(input("Please select the sauce: "))

    if sauce_choice == 1:
        pizza = Olives(pizza)
    elif sauce_choice == 2:
        pizza = Mushrooms(pizza)
    elif sauce_choice == 3:
        pizza = GoatCheese(pizza)
    elif sauce_choice == 4:
        pizza = Meat(pizza)
    elif sauce_choice == 5:
        pizza = Onions(pizza)
    elif sauce_choice == 6:
        pizza = Corn(pizza)

    # Get the total cost of the pizza object and print it to the console
    total_cost = str(pizza.get_cost())
    print("Your total cost is: " + total_cost + "$")

    # Prompt the user to enter their personal information
    name = input("Please enter your name: ")
    id_number = input("Please enter your ID number: ")
    credit_card_number = input("Please enter your credit card number: ")
    credit_card_password = input("Please enter your credit card password: ")

    # Get the description of the pizza object and the current time
    description = pizza.get_description()
    time_order = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write the order details to a csv file
    with open('Orders_Database.csv', 'a', newline='') as csv_file:
        fieldnames = ['Name', 'ID Number', 'Credit Card Number', 'Description',
                      'Time Order', 'Total Cost', 'Credit Card Password']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writerow({'Name': name, 'ID Number': id_number, 'Credit Card Number': credit_card_number,
                         'Description': description, 'Time Order': time_order, 'Total Cost': total_cost + "$",
                         'Credit Card Password': credit_card_password})

print(main())