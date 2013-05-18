def hotel_cost(nights):
	return nights * 140

bill = hotel_cost(5)

def add_monthly_interest(balance):
	return balance * (1 + (0.15 / 12))

def make_payment(payment, balance):
	new_balance = balance - payment
	x = add_monthly_interest(new_balance)    
	return "You still owe: " + str(x)
	
print make_payment(100, bill)