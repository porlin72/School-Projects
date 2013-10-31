def hotel_cost(nights):
    costs = nights*140
    return costs
    
def plane_ride_cost(city):
    # city.lower()
    if city == "Charlotte":
        price = 183
        return price
    elif city == "Tampa":
        price = 220
        return price
    elif city == "Pittsburgh":
        price = 222
        return price
    elif city == "Los Angeles":
        price = 475
        return price
    else:
        return "Invalid Input"
        
def rental_car_cost(days):
    rental = days*40
    if days >= 0 and days < 3:
        return rental
    elif days >= 3 and days < 7:
        rental -= 20
        return rental
    elif days >= 7:
        rental -= 50
        return rental
    else:
        return "Invalid Input"
        
def trip_cost(city,days,spending_money):
    sum = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    return sum
    
print trip_cost("Los Angeles", 5, 600)