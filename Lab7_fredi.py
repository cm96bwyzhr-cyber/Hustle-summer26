
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
        print("Invalid choice.")

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
    