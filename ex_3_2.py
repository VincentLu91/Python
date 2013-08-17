'''
Here, insert "break" after the "Good guess!" print statement. "break" will
terminate the while loop so that users do not have to continue guessing after
they found the number. If the user does not guess the number at all print
"Sorry but that was not very successful" (use else for this)
'''
counter = 1
while counter <= 5:
	number = input("Type in the " + str(counter) + " number: ")
	if number == 5:
		print "Good guess!"
		break
	else:
		if counter < 5:
			print "Try again!"
			counter = counter + 1
		else:
			print "Sorry but that was not very successful"
			break
# now that we finish the loop:
print "Game over."
