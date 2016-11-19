#!/usr/bin/python

import random

def main():
	randomArray = []
	for x in xrange(1,100):
		randomArray.append(random.randrange(500))
	print("Random array:")
	print(randomArray)
	randomArray = mergeSort(randomArray)
	print("Sorted array:")
	print(randomArray)

def mergeSort(array):
	if(len(array) == 1):
		return array
	left = []
	right = []
	for number in range(0, len(array)):
		if number < len(array) // 2:
			left.append(array[number])
		else:
			right.append(array[number])
	finishedLeft = mergeSort(left)

	finishedRight = mergeSort(right)

	return merge(finishedLeft, finishedRight)

def merge(leftArray, rightArray):
	finishedArray = []
	while(len(leftArray) > 0 and len(rightArray) > 0):
		if leftArray[0] <= rightArray[0]:
			finishedArray.append(leftArray.pop(0))
		else:
			finishedArray.append(rightArray.pop(0))

	#append final elements from remaining array
	if len(leftArray) > 0:
		finishedArray += leftArray
	else:
		finishedArray += rightArray
	
	return finishedArray

if __name__ == '__main__':
	main()
