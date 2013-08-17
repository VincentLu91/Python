'''
Create a list that contains the names of 5 students of this class. (Do not
ask for input to do that, simply create a list). Print the list. Ask the
user to input one more name and append it to the list. Print the list. Ask a
user to input a number. Print the name that has that number as index. Add
"John Smith" and "Mary Miller" at the beginning of the list (by using "+").
Print the list.
'''
students = ["Mary Miller", "Thomas Anderson", "Winnie Louie"]
print "The list of students is ", students
append_student = raw_input("Add a new student: ")
students.append(append_student)
print "The list of students is ", students
number = input("Add a number: ")
print "student ", number + 1, ":", students[number]
students = ["John Smith", "Mary Miller"] + students
print "The list of students is ", students
