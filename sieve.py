#!/usr/bin/env python
import cmath
"""Write a function that takes a single argument n and returns a list of prime
numbers less than or equal to n using the optimized sieving algorithm
described above."""
def sieve(n):
	n_list = []
	prime = []
	for i in range(0, n-1):
		n_list.append(i+2)
	# now that we're done with building the list, let's do the actual
	# algorithm
	n_root = int(n ** 0.5) # this is the root for optimization 3
#	print n_root
	prime.append(n_list[0]) # 2 is first appended
	del n_list[0] # remove this element
	i = 0
	while i < (len(n_list)):
	  if n_list[i] % 2 == 0: # even why does this ever work? ugh C programming...
	    del n_list[i] #n_list.remove(i) 
	  i = i + 1
	  
	# this is my attempt to replicate a list for index up to n_root
	n_rootlist = []
	for i in n_list:
	  if i <= n_root:
	    n_rootlist.append(i)
	  else:
	    break
#	print n_list
#	print n_rootlist
	prime.append(n_list[0])
	# now that we're left with odd numbers, let's do optimization 2
	for i in range (len(n_rootlist)): # for loop for up to n_root
	  #for j in range(n_list):
	  j = i * i  
	  while j < (len(n_list)):
	    if n_list[j] % n_rootlist[i] == 0: # get rid of the multiple
	      del n_list[j]
	    j = j + 1
#	print n_list
	  # now that we're outside of this while loop, we append the
	  # first element to the prime list
#	i = 0
	for i in range(len(n_list)):
	  prime.append(n_list[i])
	print prime
	print "Number of primes is ", len(prime)

#final_list = sieve(30)
final_list = sieve(100)
