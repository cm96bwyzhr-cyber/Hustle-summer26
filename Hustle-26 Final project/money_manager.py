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


