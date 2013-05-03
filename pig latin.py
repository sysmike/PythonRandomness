pyg = 'ay'

original = raw_input('Enter a word to be translated into Pig Latin: ')

if len(original) > 0 and original.isalpha():
	word = original
	word.lower()
	first = word[0]
	print "Original: " + original
	if first == "a" and "e" and "i" and "o" and "u":
		new_word = word + pyg
		print "Result: " + new_word
	else:
		new_word = original
		new_word = new_word[1:] + first + pyg
		print "Result: " + new_word
else:
	print 'empty'