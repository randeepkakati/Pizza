pizza_limit = 10
burger_limit = 15
fries_limit = 30
print("Welcome to Pazzito Shop ! We make tasty Pizza, burger and fries. ")
food = input(" what would you like to eat i.e. pizza, burger or fries ? ")
quantity = int(input(" how many? "))
if food == "pizza":
    if quantity <= pizza_limit:
        print("Pizza order placed!")
    else:
        print("Sorry the available pizza limit is :" + str(pizza_limit))
elif food == "burger":
    if quantity <= burger_limit:
        print("Burger order placed!")
    else:
        print("Sorry the available burger limit is :" + str(burger_limit))
elif food == "fries":
    if quantity <= fries_limit:
        print("Fries order placed!")
    else:
        print("Sorry the available fries limit is :" + str(fries_limit))
