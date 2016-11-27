#!usr/bin/python

import random
import sys
import collections

def main():
	bigArray = initBigArray(30, 10)
	prettyPrint2dArray(bigArray)

	print "Max subarray:"
	subArray = getMaxSubarrayBrute(bigArray)
	prettyPrint2dArray(subArray)
	
	#total it up
	total = 0
	for x in xrange(len(subArray)):
		for y in subArray[x]:
			total += y
	print "Brute force total: " + str(total)

	print "Max subarray optimized: "
	subArrayOptimized = getMaxSubarrayWithPrecompute(bigArray)
	prettyPrint2dArray(subArrayOptimized)

def prettyPrint2dArray(array):
	for x in xrange(len(array)):
		for y in xrange(len(array[x])):
			sys.stdout.write('{0:3d} '.format(array[x][y]))
		sys.stdout.write('\n')
	

def initBigArray(size, maximumRange):
	arr = []
	for x in xrange(size):
		row = []
		for y in xrange(size):
			row.append(random.randrange(-maximumRange, maximumRange))
		arr.append(row)
	return arr

"""
#For a simple brute force, we can iterate with a top left and bottom right corner over the entire array. The TL corner goes from 0 to len(array) on both the x and y and the BR corner goes from TL corner to len(array). This will run in O(n^4 * getSubarrayCount()) time, and on average we can expect getSubarrayCount to work on around 1/4 the size of the full array (average of half for each dimension). This would give this algorithm a runtime bound of O(n^6).
"""
def getMaxSubarrayBrute(array):
	maxi = 0
	maxTLX = maxTLY = maxBRX = maxBRY = 0
	for tlx in xrange(len(array)):
		for tly in xrange(len(array)):
			for brx in xrange(tlx, len(array)):
				for bry in xrange(tly, len(array)):
					newMax = getSubarrayCountBrute(array, tlx, tly, brx, bry)
					if newMax > maxi:
						maxi = newMax
						maxBounds = [tlx, tly, brx, bry]
						maxTLX = tlx
						maxTLY = tly
						maxBRX = brx
						maxBRY = bry
	return [array[i][maxTLX:maxBRX + 1] for i in range(maxTLY, maxBRY + 1)]

def getSubarrayCountBrute(array, tlx, tly, brx, bry):
	count = 0
	for row in xrange(tly, bry + 1):
		for column in xrange(tlx, brx + 1):
			count += array[row][column]
	return count

"""
To reduce the amount of duplicate work that we do, we can perform a similar greedy algorithm to finding the maximum in a one dimensional array that works in linear time and constant additional space. We can precompute a running total of each row (so [-1, 2, 5] goes to [-1, 1, 6]) to be able to get the running total of any subarray in O(1) time. For example, getting the running count from index 3 to 6 is just taking the running total at 6 and subtracting the running total at 2 (making sure to have bound checks for the corner case of starting at 0).

With that, we can then look at every row combination with top [0, len(array)) and bottom [top, len(array)) in O(n^2) time and treat those sets of row as a single digit using the above computation. We can then perform the same one dimensional subarray search in linear time and with constant space, making for a total time complexity of O(n^3) and additional space of O(N^2) for the precomputed array.

The greedy algorithm on a single dimension array iterates through values and keeps track of the maximum value seen (as well as the endpoints). If the current max dips below 0 at index i, then the previous segment up is net negative up to index i and we can assume that any new maximum we compute would not use any previous segment including index i.

For this we are assuming that there are positive numbers in the original 2 dimensional array. If we want to cover the case of an array with all negative numbers, we can iterate over each single dimension problem and get the maximum
"""
def getMaxSubarrayWithPrecompute(array):
	totalArray = []
	maxCount = 0

	#precompute
	for row in array:
		total = 0
		totalRow = []
		for x in xrange(len(row)):
			total += row[x]
			totalRow.append(total)
		totalArray.append(totalRow)

	maxVal = 0
	maxLeft = maxRight = maxTop = maxBottom = 0
	for left in xrange(len(array)):
		for right in xrange(left, len(array)):
			returnVal = getMaxSubarray(totalArray, left, right, array)
			if returnVal.max > maxVal:
				maxVal = returnVal.max
				maxTop = returnVal.top
				maxBottom = returnVal.bottom
				maxLeft = left
				maxRight = right

	print "Optimized max of: " + str(maxVal)

	return [array[i][maxLeft:maxRight + 1] for i in range(maxTop, maxBottom + 1)]

SubArray = collections.namedtuple('SubArray', ['max', 'top', 'bottom'])

# This returns the maximum subarray using a two dimensional totals array with a set left and right
def getMaxSubarray(totalArray, left, right, array):
	currentMax = currentTotal = 0
	currentTop = 0
	maxTop = maxBottom = 0
	for x in xrange(len(totalArray[left])):
		nextVal = totalArray[x][right]
		if left > 0:
			nextVal -= totalArray[x][left - 1]
		currentTotal += nextVal

		if currentTotal > currentMax:
			currentMax = currentTotal
			maxBottom = x
			maxTop = currentTop
		if currentTotal < 0:
			if x < len(totalArray) - 1:
				currentTotal = 0
				currentTop = x + 1

	return SubArray(currentMax, maxTop, maxBottom)

if __name__ == '__main__':
	main()
