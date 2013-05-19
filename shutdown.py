def shut_down(s):
	x = s.lower()
	if x == "yes":
		return "Shutting down..."
	if x == "no":
		return "Shutdown aborted!"
	else:
		return "Sorry, I didn't understand you."