menu = "Black Coffee, Espresso, Latte, Cappucino, Frappuccino"
name = input("What is your name?")

#Ask the customer what they would like from the menu and store it in the variable order.
order= input(name + ", what would you like to drink?\n" + menu + "\n")

#Ask the customer how many coffees thye want and store it in the variable Quanitity
quantity = input("How many coffees would you like?\n")

#Price for coffee

if order == "Frappuccino":
    price = 13
elif order == "Espresso":
    price = 5
elif order == "Black Coffee":
    price = 3
elif order == "Cappucino":
    price = 7
elif order == "Latte":
    price = 9
    
else:
    print("Sorry, we don't have that here.")
    price = 0

print(price * quantity)

#Latte do you want whipped cream? yes =11 no =9
