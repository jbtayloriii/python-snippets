#!/usr/bin/python

import trees
import treePrint
import random

def main():
	valueList = range(1,25)
	root = trees.constructRandomBinarySearchTree(valueList)
	treePrint.printTree(root)

	randomNumbers = range(1,15)
	values = []
	values.append(randomNumbers.pop(random.randrange(len(randomNumbers))))
	values.append(randomNumbers.pop(random.randrange(len(randomNumbers))))
	print("Looking for values: " + str(values))
	ancestorValue = findCommonAncestor(root, values).value
	print('The common ancestor of {0} and {1} is {2}'.format(str(values[0]), str(values[1]), str(ancestorValue)))

#Finds the first common ancestor of two (or more) distinct values in a tree.
# Works for any sort of binary tree, operates in O(n) time where n is the number of nodes in the tree
# and in O(h) space (in memory for recursion) where h is the height of the tree
def findCommonAncestor(node, values):
	if node is None:
		return None

	leftNode = findCommonAncestor(node.left, values)
	rightNode = findCommonAncestor(node.right, values)
	if leftNode is None and rightNode is None:
		if node.value in values:
			return node
		return None
	elif (not leftNode is None) and (not rightNode is None):
		return node
	else:
		#one child has a searched value, either return ourself (if we contain the other value), or
		#pass the child up
		if node.value in values:
			return node
		elif (not leftNode is None):
			return leftNode
		else:
			return rightNode

if __name__ == '__main__':
	main()
