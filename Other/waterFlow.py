#!usr/bin/python

import random
import sys

def main():
	arr = initializeArray(20, 10)
	print "Test array: " + str(arr)
	printArrayVisual(arr)
	print "water in array: " + str(getWaterFlow(arr))

def initializeArray(size, maxHeight):
	array = []
	for x in xrange(size):
		array.append(random.randrange(maxHeight + 1))
	return array

def printArrayVisual(arr):
	maxHeight = 0
	for r in arr:
		if r > maxHeight:
			maxHeight = r
	for height in xrange(maxHeight, 0, -1):
		for x in xrange(len(arr)):
			if arr[x] >= height:
				sys.stdout.write("X")
			else:
				sys.stdout.write(" ")
		sys.stdout.write("\n")
	sys.stdout.write("X" * len(arr) + "\n")

def getWaterFlow(arr):
	maxHeight = 0
	heightArr = []
	#sweep right, get max height of previous left sides
	for index in xrange(len(arr)):
		height = arr[index]
		if height > maxHeight:
			maxHeight = height
		heightArr.append(maxHeight)

	#sweep left, get max height of previous right sides
	#if the right side is lower than the left side, we adjust the max water height (minimum of max on left and right)
	maxHeight = 0
	for index in xrange(len(arr) - 1, -1, -1):
		height = arr[index]
		if height > maxHeight:
			maxHeight = height
		if maxHeight < heightArr[index]:
			heightArr[index] = maxHeight

	#calculate water here, make sure not to subtract if we are at a peak
	water = 0
	for x in xrange(len(arr)):
		if heightArr[x] - arr[x] > 0:
			water += heightArr[x] - arr[x]

	return water	

if __name__ == "__main__":
	main()
