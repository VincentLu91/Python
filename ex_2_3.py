'''
Write a program that asks users for their favourite colour. Create the 
following output (assuming "red" is the chosen colour). Use '+' and '*'
red red red red red red red red red red
red                                 red
red                                 red
red red red red red red red red red red
'''
colour = raw_input("Enter your favourite colour: ")
line1 = 10*(colour + " ")
whitespace = ((len(colour) * " ") + " ") * 8
line2 = colour + " " + whitespace + colour
print line1
print line2
print line2
print line1
