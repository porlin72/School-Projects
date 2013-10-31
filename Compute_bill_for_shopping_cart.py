shopping_list = ["banana", "orange", "apple"]

stock = { "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = { "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        for stuff in stock and prices:
            if item == stuff:
                if stock[stuff] > 0:
                    total += prices[item]
                    stock[item] -=1
                else:
                    total += 0
            else:
                print "Item not in stock"
    return total