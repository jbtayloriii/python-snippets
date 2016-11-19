#!/usr/bin/python

import random

def main():
	randomArray = []
	for x in xrange(1,100):
		randomArray.append(random.randrange(500))
	print("Random array:")
	print(randomArray)
	quickSort(randomArray)
	print("Sorted array:")
	print(randomArray)

def quickSort(array):
	quickSortInternal(array, 0, len(array))


def quickSortInternal(array, low, high):
	if (low >= high):
		return
	pivot = array[high - 1]
	counter = low
	for x in range(low, high - 1):
		if array[x] <= pivot:
			swap(array, x, counter)
			counter += 1
	swap(array, high - 1, counter)
	quickSortInternal(array, low, counter - 1)
	quickSortInternal(array, counter + 1, high)

def swap(array, pos1, pos2):
	temp1 = array[pos1]
	array[pos1] = array[pos2]
	array[pos2] = temp1
	

if __name__ == '__main__':
	main()
