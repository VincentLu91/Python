'''
Create a list that contains the names of 5 students of this class. (Do not
ask for input to do that, simply create a list). Print the list. Ask the
user to input one more name and append it to the list. Print the list. Ask a
user to input a number. Print the name that has that number as index. Add
"John Smith" and "Mary Miller" at the beginning of the list (by using "+").
Print the list.
Continue with the script from 1.1): Print the list. Remove the last name from
the list. Print the list. Ask a user to type a name. Check whether that name
is in the list: if it is then delete it from the list. Otherwise add it at
the end. Create a copy of the list in reverse order. Print the original list
and the reverse list
'''
students = ["Paul Miller", "Kathy Jones", "Susan Smith", "John Doe",
"James Black"]

print "The following students are in the class:", students

del students[-1]
print "The following students are in the class:", students

another_student = raw_input("Enter the name of a student to be added/deleted: ")
if another_student in students:
        students.remove(another_student)
else:
        students.append(another_student)

print "The following students are in the class:", students

more_students = students[:]

more_students.reverse()
print students
print more_students
