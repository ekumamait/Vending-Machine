"""This displays the menu"""

print("---------- VENDING MACHINE --------------")

print("Number -- Drink")
print("--- 1 --- Coca-Cola")
print("--- 2 --- Pepsi")
print("--- 3 --- Sprite")
print("--- 4 --- Mountain Dew")

choice = input("Enter Number to buy a Drink: ")

class Vendor:
    def __init__(self):
        self.switcher = {1:"cola", 2:"pepsi", 3:"sprite", 4:"dew"}        

    def vender(self,choice):

        func = self.switcher.get(choice[0], "nothing")
        return func()
        
    def cola(self):
        price = input("Enter 100 to buy a Drink: ")
        cost = 100
        if price == cost:
            return "Coca-Cola"
        elif price < cost:
            newprice = input("Enter more to buy a Drink: ")
            if newprice + price == cost:
                return "Coca-Cola"
            else:
                return "oops"     
        elif price > cost:
            balance = price - cost
            return "Coca-Cola " + balance        
        else:
            return "oops"

    def pepsi(self):
        price = input("Enter 50 to buy a Drink: ")
        cost = 50
        if price == cost:
            return "Pepsi"
        elif price < cost:
            newprice = input("Enter more to buy a Drink: ")
            if newprice + price == cost:
                return "Pepsi"
            else:
                return "oops"    
        elif price > cost:
            balance = price - cost
            return "Coca-Cola " + balance        
        else:
            return "oops"    

    def sprite(self):
        price = input("Enter 70 to buy a Drink: ")
        cost = 70
        if price == cost:
            return "Sprite"
        elif price < cost:
            newprice = input("Enter more to buy a Drink: ")
            if newprice + price == cost:
                return "Sprite"
            else:
                return "oops"    
        elif price > cost:
            balance = price - cost
            return "Sprite " + balance
        else:
            return "oops" 

    def dew(self):  
        price = input("Enter 80 to buy a Drink: ")
        cost = 80
        if price == cost:
            return "Mountain Dew"  
        elif price < cost:
            newprice = input("Enter more to buy a Drink: ")
            if newprice + price == cost:
                return "Mountain Dew"
            else:
                return "oops"    
        elif price > cost:
            balance = price - cost
            return "Mountain Dew " + balance
        else:
            return "oops"
        

