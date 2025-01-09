#Create a class  Inventory  to manage stock levels. Add methods
#to add, remove, and query items, including checks for insufficient
#stock


class Inventory:
    def __init__(self):
        self.stock = {}
        
    def add_item(self, item, quantity):
        if item in self.stock:
            self.stock[item] += quantity
        else:
            self.stock[item] = quantity
        print("Item added successfully")
        
    def remove_item(self, item, quantity):
        if item in self.stock:
            if self.stock[item] >= quantity:
                self.stock[item] -= quantity
                print("Item removed successfully")
            else:
                print("Insufficient stock")
        else:
            print("Item not found")
            
    def query_item(self, item):
        if item in self.stock:
            print("Quantity of", item, "is", self.stock[item])
        else:
            print("Item not found")

def main():
    inventory = Inventory()
    while True:
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Query Item")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.add_item(item, quantity)
        elif choice == 2:
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.remove_item(item, quantity)
        elif choice == 3:
            item = input("Enter item name: ")
            inventory.query_item(item)
        elif choice == 4:
            break
        else:
            print("Invalid choice")

main()