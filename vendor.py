
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
        print("Here is your Coca-Cola. Enjoy")
    elif price < cost:
        newprice = int(input("Enter more to buy a coca-cola: "))
        if newprice + price == cost:
            print("Here is your Coca-Cola. Enjoy")
        else:
            print("oops! invalid input")     
    elif price > cost:
        balance = price - cost
        print("Here is your Coca-Cola. Enjoy & Balance of "  + str(balance))        
    else:
        print("oops! invalid input")

def pepsi():
    """A function to operate on pepsi option"""
    price = int(input("Enter 50 to buy a pepsi: "))
    cost = 50
    if price == cost:
        print("Here is your Pepsi. Enjoy")
    elif price < cost:
        newprice = int(input("Enter more to buy a pepsi: "))
        if newprice + price == cost:
            ("Here is your Pepsi. Enjoy")
        else:
            print("oops! invalid input")    
    elif price > cost:
        balance = price - cost
        print("Here is your Pepsi. Enjoy & Balance of " + str(balance))        
    else:
        print("oops! invalid input")    

def sprite():
    """A function to operate on sprite option"""
    price = int(input("Enter 70 to buy a sprite: "))
    cost = 70
    if price == cost:
        print("Here is your Sprite. Enjoy")
    elif price < cost:
        newprice = int(input("Enter more to buy a sprite: "))
        if newprice + price == cost:
            print("Here is your Sprite. Enjoy")
        else:
            print("oops! invalid input")    
    elif price > cost:
        balance = price - cost
        print("Here is your Sprite. Enjoy & Balance of " + str(balance))
    else:
        print("oops! invalid input") 

def dew():  
    """A function to operate on Mountain option"""
    price = int(input("Enter 80 to buy a Mountain option: "))
    cost = 80
    if price == cost:
        print("Here is your Mountain Dew. Enjoy")  
    elif price < cost:
        newprice = int(input("Enter more to buy a Mountain option: "))
        if newprice + price == cost:
            print("Here is your Mountain Dew. Enjoy")
        else:
            print("oops! invalid input")    
    elif price > cost:
        balance = price - cost
        print("Here is your Mountain Dew. Enjoy & Balance of" + str(balance))
    else:
        print("oops! invalid input")

switcher = {1: cola, 2: pepsi, 3: sprite, 4: dew}
lines = [1, 2, 3, 4]

for line in lines:
    func = switcher[line]
    func()

# func = switcher.get(choice, "invalid input")
# return fun()
 