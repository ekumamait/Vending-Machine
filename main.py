from app.vendor import Vendor

"""This displays the menu"""

print("-- VENDING MACHINE --")

print("\n *Number  *Drink")
print("\n--- 1 --- Coca-Cola")
print("--- 2 --- Pepsi")
print("--- 3 --- Sprite")
print("--- 4 --- Mountain Dew")

choice = input("\nEnter Number to buy a Drink: ")

if __name__ == '__main__':
    donald = Vendor()
    print(donald)    