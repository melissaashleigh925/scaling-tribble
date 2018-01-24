# 12/11/2016
# Python 3.4
# Program generates 10 random integers from 20 to 30, puts them in a list, sorts the list, finds the sum, and average of numList, finds the median of the sorted list, and shows how many numbers are evenly divisable by two.


import random

numList = []
sortedList = []
count = 0

print("Generating a list with 10 random numbers between 20 and 30:")
print("")
print("When a number is divisable by two, it will be shown.")
print("")


for randomNumber in range(0,10):
	randomNumber = random.randint(20,30)
	numList.append(randomNumber)
	count += randomNumber
	
	if randomNumber%2 == 0:
	
		print("This number is divisable by two:", randomNumber)
print("")  
print("Your random generated list:",numList)
print("The sum of random generated list is:",count)
print("The average of random generated list is:", "{:.2f}".format( count/10))
    
while numList:

	minimum = numList[0]
	for x in numList:
		if x < minimum:
			minimum = x
	sortedList.append(minimum)
	numList.remove(minimum)
	
middle = len(sortedList)//2
median = (sortedList[middle] + sortedList[middle -1]) / 2
print("")
print("The sorted random generated list is:",sortedList)
print("The median of your sorted list is:",median)	

'''
Example Output 1:

Generating a list with 10 random numbers between 20 and 30:

When a number is divisable by two, it will be shown.

This number is divisable by two: 26
This number is divisable by two: 24
This number is divisable by two: 28
This number is divisable by two: 22
This number is divisable by two: 20

Your random generated list: [26, 29, 27, 24, 28, 21, 22, 27, 20, 25]
The sum of random generated list is: 249
The average of random generated list is: 24.90

The sorted random generated list is: [20, 21, 22, 24, 25, 26, 27, 27, 28, 29]
The median of your sorted list is: 25.5

'''
'''
Example Output 2:

Generating a list with 10 random numbers between 20 and 30:

When a number is divisable by two, it will be shown.

This number is divisable by two: 26
This number is divisable by two: 20

Your random generated list: [21, 21, 26, 25, 25, 21, 29, 21, 20, 23]
The sum of random generated list is: 232
The average of random generated list is: 23.20

The sorted random generated list is: [20, 21, 21, 21, 21, 23, 25, 25, 26, 29]
The median of your sorted list is: 22.0
'''

