#!usr/bin/python

import random
import waterFlow

def main():
	size = 20
	maxNumber = 10
	subArrayMaxSize = 4
	arr = waterFlow.initializeArray(size, maxNumber)
	print "Large array: " + str(arr)
	subArray = []
	for x in xrange(len(arr)):
		if not arr[x] in subArray:
			subArray.append(arr[x])

	while len(subArray) > subArrayMaxSize:
		subArray.pop(random.randrange(len(subArray)))
	print "Subarray: " + str(subArray)

	arraySlice = getSmallestContainingArray(arr, subArray)
	print "Array slice from " + str(arraySlice[0]) + " to " + str(arraySlice[1]) + " inclusive"
	print arr[arraySlice[0]:arraySlice[1] + 1]

# To determine the smallest containing array of all values in sub (assuming we have good inputs), we have to
# loop over sub and search for each value in arr. We keep track of how far back the current number is, with
# 0 indicating that this array index has the value and x meaning that it is at position i - x. We then keep track of
# the farthest (maximum) back digit of the ones in sub that we've seen. Finally, we simply need to find the smallest
# value in our maximum array and return that slice from i - x to i, where x is the smallest value in the maximum array.
def getSmallestContainingArray(arr, sub):
	farthestArr = []

	#initialization
	for x in xrange(len(arr)):
		farthestArr.append(0)

	for value in sub:
		countback = 0
		for x in xrange(len(arr)):
			if arr[x] == value:
				countback = 0
			else:
				countback += 1
			if countback > farthestArr[x]:
				farthestArr[x] = countback

	min = len(arr)
	start = stop = -1
	for x in xrange(len(farthestArr)):
		if farthestArr[x] < min and (x - farthestArr[x]) >= 0:
			min = farthestArr[x]
			stop = x
			start = x - min
	return [start, stop]
		

if __name__ == '__main__':
	main()
