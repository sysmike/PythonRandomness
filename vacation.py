def hotel_cost(nights):
	costs = nights * 140
	return costs
	
def plane_ride_cost(city):
	if city == "Charlotte":
		return 183
	elif city == "Tampa":
		return 220
	elif city == "Pittsburgh":
		return 222
	elif city == "Los Angeles":
		return 475
	else:
		return "Dafaq?"
		
def rental_car_cost(days):
	if days < 3:
		cost_car = 40 * days
		return cost_car
	elif days >= 3 and days < 7:
		cost_car = 40 * days - 20
		return cost_car
	elif days >= 7:
		cost_car = 40 * days - 50
		return cost_car
	else:
		return "Challenge accepted" 
		
def trip_cost(city, days, spending_money):
	return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money
	
result = trip_cost("Los Angeles",5 , 600)
print result