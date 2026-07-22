import random

# ticket 1 Item blueprint Own tab

class book():
    def __init__(self, name, price):
        self.name = name
        self.price = price



    # Ticket 3 -  Price Guard(Encapsulation)
    def set_price(self, amount):
        if amount < 0:
            print("price cannot be below $0")
        else:
            self.price = amount
         



    # Ticket 5- polymorphism
    def deliver(self):
        print(f"{self.name} is being shipped to the customer.!")
    
    
        


# Ticket 4 -Second Kind of Item (Inheritance)
class Slide(book):
    def deliver(self):
        print(self.name, "has been added")


# TICKET 2 - Real Items

item1 = book("Harry poter", 10)
item2 = Slide("avatar", 150)


# Extension Ticket 2 - Sale
item2.set_price(100)
print(item2.name, "is on sale for $", item2.price)



# Test Ticket 3
#item1.set_price(-5)

# Test Ticket 5
item1.deliver()


# Ticket 6
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(item.name, "added!")


    # Ticket 9
    def checkout(self):
        total = 0

        print("\nCheckout:")

        for item in self.items:
            item.deliver()
            total += item.price

        print("Total: $", total)


#Ticket 7
# Ticket 7
store = {
    "1": item1,
    "2": item2
}

cart = Cart()


# Extension Ticket 1 - Random Welcome
welcome_messages = [
    "Hey there, happy shopping!",
    "Welcome to our store!",
    "Thanks for shopping with us!"
]

print(random.choice(welcome_messages))


# Extension Ticket 3 - Show Menu
print("\nHere is what we have:")

for number, item in store.items():
    print(number + ": " + item.name + " - $" + str(item.price))


# Ask for the customer's name BEFORE the shopping starts
customer = input("What is your name? ")
print("Welcome,", customer + "!")



# Ticket 8
while True:
    choice = input("Pick 1, 2, or 'done': ")

    if choice == "done":
        break

    elif choice in store:
        cart.add(store[choice])

    else:
        # Extension Ticket 4
        print("Sorry, that's not on the menu!")



# Extension Ticket 5 - Receipt
print("----- Your receipt -----")

for item in cart.items:
    print(item.name + " ..... $" + str(item.price))


# Extension Ticket 6 - Count Order
print("You bought " + str(len(cart.items)) + " items.")



# These lines go AFTER the while loop ends
cart.checkout()
print("Thank you for shopping with us,", customer + "!")



#ticket 8
while True:
    choice = input("Pick 1, 2, or 'done': ")

    if choice == "done":
        break

    elif choice in store:
        cart.add(store[choice])

    else:
        print("Invalid choice.")


# Ticket 9
    
    cart.checkout()
    
