'''
Modify the program so that it asks users whether they want to guess again 
each time. Use two variables, number for the number and answer for the 
answer to the question whether they want to continue guessing. The program
stops if the user guesses the correct number or answers "no". (In other words,
the program continues as long as a user has not answered "no" and has not
guessed the correct number.)
'''
number = -1
again = "yes"
while number != 5 and again != "no":
    number = input("Guess the lucky number: ")
    if number != 5:
        print "That is not the lucky number"
        again = raw_input("Would you like to guess again? ")
