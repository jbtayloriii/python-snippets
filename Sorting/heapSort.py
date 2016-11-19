#!/usr/bin/python

import random
import heap

def main():
	randomArray = []
	for x in xrange(1,100):
		randomArray.append(random.randrange(500))
	print("Random array:")
	print(randomArray)
	randomArray = heapSort(randomArray)
	print("Sorted array:")
	print(randomArray)

def heapSort(array):
	heapObj = heap.minHeap()
	sortedArray = []
	for x in xrange(len(array)):
		heapObj.add(array[x])
	while not heapObj.peekMin() is None:
		sortedArray.append(heapObj.getMin())
	return sortedArray

if __name__ == '__main__':
	main()
