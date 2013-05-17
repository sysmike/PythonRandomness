def distance_from_zero(p):
	if p.type() == int:
		return p.abs()
	elif p.type() == float:
		return p.abs()
	else:
		return "Not an integer or float!"
distance_from_zero(1)