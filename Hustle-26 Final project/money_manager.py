#=================================================================================================================================================================
#|| Name: Fredi                                                                                                                                                 ||
#|| Program Title: The Manager App                                                                                                                              ||
#|| Date: Aug 2                                                                                                                                                 ||
#|| Time: 9:29                                                                                                                                                  ||
#|| Class: Hustle Program                                                                                                                                       ||
#=================================================================================================================================================================


#=================================================================================================================================================================
#||  Blueprint                                                                                                                                                  ||
#|| Describes one thing on your list. Everything on the list gets built from this. It also has one method that says no to a bad number, like a price below zero.||
#=================================================================================================================================================================

class ShoppingItem:
    def __init__(self, name, price):
        self.name = name
        self.price = 0
        self.set_price(price)

#=======================================================================================================
#|| The Price Check                                                                                     ||
#|| This checks the price. If the number is bad, it changes it to 0 so the item is safe.                ||
#=======================================================================================================

    def set_price(self, price):
        if price < 0:
            print("Price cannot be negative. Setting price to $0.")
            self.price = 0
        elif price > 10000:
            print("That price is too high. Setting price to $0.")
            self.price = 0
        else:
            self.price = price

    def display(self):
        print(f"Item: {self.name}")
        print(f"Price: ${self.price:.2f}")


#==========================================================================================================
#|| Kind 1                                                                                               ||
#|| The first kind of that thing. It gets everything the blueprint has, plus one extra detail of its own.||
#==========================================================================================================

class Clothing(ShoppingItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def display(self):
        print("===== Clothing =====")
        super().display()
        print(f"Size: {self.size}")


#=======================================================================================================
#|| Kind 2                                                                                            ||
#|| The second kind. Same deal, but a different extra detail so it acts a little different from Kind 1||
#=======================================================================================================

class Electronics(ShoppingItem):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

    def display(self):
        print("===== Electronics =====")
        super().display()
        print(f"Brand: {self.brand}")


#=======================================================================================================
#|| Kind 3                                                                                            ||
#|| Books is another type of ShoppingItem. It gets the name and price from the blueprint,             ||
#|| but it also adds its own detail called author.                                                    ||
#=======================================================================================================

class Books(ShoppingItem):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author

    def display(self):
        print("===== Books =====")
        super().display()
        print(f"Author: {self.author}")


#=======================================================================================================
#|| Kind 4                                                                                            ||
#|| Food is another type of ShoppingItem. It gets the name and price from the blueprint,              ||
#|| but it also adds its own detail called expiration date.                                           ||
#=======================================================================================================

class Food(ShoppingItem):
    def __init__(self, name, price, expiration):
        super().__init__(name, price)
        self.expiration = expiration

    def display(self):
        print("===== Food =====")
        super().display()
        print(f"Expiration Date: {self.expiration}")


#===============================================================================================
#|| The Boss                                                                                  ||
#|| Holds the whole list. Shows the menu, adds new things to the list and adds up the numbers.||
#===============================================================================================

class ShoppingManager:

    def __init__(self):
        # This makes it start with 7 items
        self.items = [
            Clothing("Gap Hoodie", 59.99, "Medium"),
            Clothing("Essentials Sweatpants", 140.00, "Large"),
            Electronics("Headphones", 80.00, "Sony"),
            Electronics("iPhone 17", 799.00, "Apple"),
            Clothing("Shoes", 70.00, "10"),
            Books("I WILL TEACH YOU HOW TO BE RICH", 29.99, "Ramit Sethi"),
            Food("Chocolate", 3.99, "08/20/2026")
        ]


    #=======================================================================================================
    #|| All the Items are shown                                                                          ||
    #|| This shows every item in the shopping list and displays its information.                         ||
    #=======================================================================================================

    def show_items(self):
        if len(self.items) == 0:
            print("The shopping list is empty.")
            return

        print("===== Shopping List =====")

        for i, item in enumerate(self.items, 1):
            print(f"Item #{i}")
            item.display()


    #=======================================================================================================
    #|| New Item are added                                                                                ||
    #|| This lets the user add a new item and choose what type it is.                                     ||
    #=======================================================================================================

    def add_item(self):
        print("1. Clothing")
        print("2. Electronics")
        print("3. Books")
        print("4. Food")

        try:
            choice = int(input("Choose a type: "))
        except ValueError:
            print("Please enter a number.")
            return

        if choice not in [1, 2, 3, 4]:
            print("Invalid choice.")
            return

        name = input("Item name: ")

        try:
            price = float(input("Price: $"))
        except ValueError:
            print("Please enter a valid price.")
            return


        if choice == 1:
            size = input("Size: ")
            self.items.append(Clothing(name, price, size))

        elif choice == 2:
            brand = input("Brand: ")
            self.items.append(Electronics(name, price, brand))

        elif choice == 3:
            author = input("Author: ")
            self.items.append(Books(name, price, author))

        elif choice == 4:
            expiration = input("Expiration Date: ")
            self.items.append(Food(name, price, expiration))

        print("Item added successfully!")


    #=======================================================================================================
    #|| The total of the Cost                                                                             ||
    #|| This adds all the prices together and shows the final amount.                                     ||
    #=======================================================================================================

    def total_cost(self):
        total = 0

        for item in self.items:
            total += item.price

        print(f"Total Cost: ${total:.2f}")


    #=======================================================================================================
    #|| The Main Menu of the App                                                                          ||
    #|| This controls the program and lets the user choose what they want to do.                          ||
    #=======================================================================================================

    def menu(self):
        while True:
            print("========== Shopping Manager ==========")
            print("1. Show Shopping List")
            print("2. Add Item")
            print("3. Show Total Cost")
            print("4. Clear Shopping List")
            print("5. Quit")

            try:
                choice = int(input("\nChoose an option: "))
            except ValueError:
                print("Please enter a number.")
                continue


            if choice == 1:
                self.show_items()

            elif choice == 2:
                self.add_item()

            elif choice == 3:
                self.total_cost()

            elif choice == 4:
                self.items.clear()
                print("Shopping list cleared.")

            elif choice == 5:
                print("Thanks for using Shopping Manager!")
                break

            else:
                print("Invalid menu choice.")


#=======================================================================================================
#|| Start of the Program                                                                              ||
#|| This starts the Shopping Manager app.                                                             ||
#=======================================================================================================

def main():
    app = ShoppingManager()
    app.menu()


if __name__ == "__main__":
    main()