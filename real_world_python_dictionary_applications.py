#1. Real-World Python Dictionary Applications

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
    #Add a new category called "Beverages" with at least two items.
restaurant_menu["Beverages"] = {"Water": 1.75, "Orange juice": 3.50}

    #Update the price of "Steak" to 17.99.
restaurant_menu['Main Course']['Steak'] = 20.99

    #Remove "Bruschetta" from "Starters".
del restaurant_menu["Starters"]["Bruschetta"]

#test
#print(restaurant_menu)





