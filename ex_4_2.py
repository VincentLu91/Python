'''
Ask the user to type something (use raw_input). To find out whether the input
was a number, compare whether the input is after "0" and before ":" in
alphabetical order. If it is a number convert it into an integer. Then print
the input and its type. (Note: this won't work if the user enters a real
number.)
'''
n = raw_input("Type something: ")
if (n > "0") and (n < ":"):
	n = int(n) # convert input number to integer
print "The input is ", n
print "The type of this input is ", type(n)
