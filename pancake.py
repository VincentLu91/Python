#!/usr/bin/env python

"""Write a function that sorts a list of unique positive integers into
ascending order using the pancake sorting algorithm"""

import operator

def min_test(list):
        max_x = list.index(min(list))
        return min_x


def pancake_sorting(arr):
	# find maximum element of list, store it in a variable
	# loop from that element to second largest element, flip those
	# then move to next element, recursively call it but that element
	print "Prior to pancake sorting, the list is: "
	print arr
	for i in range(len(arr)):
		print "Flipping iteration ", i
		j =  i + min_test(arr[i:])
		arr[j:] = reversed(arr[j:])
		print arr
		# flip from end of list to current i
		arr[i:] = reversed(arr[i:]) 
		print arr
	# after the loop, I noticed that the elements are in descending order
	# in the end, reverse everything so that they're ascending order
	print "After pancake sorting, the list is: "
	#arr.reverse()
	print arr	
some_list = [1, 6, 3, 5, 7, 2, 8, 4]
pancake_sorting(some_list)
