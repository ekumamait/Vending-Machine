
"""This displays the menu"""

print("\n-- VENDING MACHINE --")

print("\n *Number  *Drink")
print("\n--- 1 --- Coca-Cola")
print("--- 2 --- Pepsi")
print("--- 3 --- Sprite")
print("--- 4 --- Mountain Dew")

choice = input("\nEnter Number to buy a Drink: ")

def cola():
    """A function to operate on coca-cola option"""
    price = int(input("Enter 100 to buy a coca-cola: "))
    cost = 100
    if price == cost:
        return "Coca-Cola"
    elif price < cost:
        newprice = int(input("Enter more to buy a coca-cola: "))
        if newprice + price == cost:
            return "Coca-Cola"
        else:
            return "oops"     
    elif price > cost:
        balance = price - cost
        return "Coca-Cola " + balance        
    else:
        return "oops"

def pepsi():
    """A function to operate on pepsi option"""
    price = int(input("Enter 50 to buy a pepsi: "))
    cost = 50
    if price == cost:
        return "Pepsi"
    elif price < cost:
        newprice = int(input("Enter more to buy a pepsi: "))
        if newprice + price == cost:
            return "Pepsi"
        else:
            return "oops"    
    elif price > cost:
        balance = price - cost
        return "Coca-Cola " + balance        
    else:
        return "oops"    

def sprite():
    """A function to operate on sprite option"""
    price = int(input("Enter 70 to buy a sprite: "))
    cost = 70
    if price == cost:
        return "Sprite"
    elif price < cost:
        newprice = int(input("Enter more to buy a sprite: "))
        if newprice + price == cost:
            return "Sprite"
        else:
            return "oops"    
    elif price > cost:
        balance = price - cost
        return "Sprite " + balance
    else:
        return "oops" 

def dew():  
    """A function to operate on Mountain option"""
    price = int(input("Enter 80 to buy a Mountain option: "))
    cost = 80
    if price == cost:
        return "Mountain Dew"  
    elif price < cost:
        newprice = int(input("Enter more to buy a Mountain option: "))
        if newprice + price == cost:
            return "Mountain Dew"
        else:
            return "oops"    
    elif price > cost:
        balance = price - cost
        return "Mountain Dew " + balance
    else:
        return "oops"

switcher = {"one": cola, "two": pepsi, "three": sprite, "four": dew}
lines = ["one", "two", "three", "four"]

for line in lines:
    func = switcher[line]
    func()
            
 