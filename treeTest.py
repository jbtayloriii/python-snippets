#!/usr/bin/python

import trees
import treePrint
import random

def main():
	root = trees.constructRandomBinarySearchTree(range(1,20))
	
	print("Tree picture:")
	treePrint.printTree(root)

	if root.contains(2):
		print("This tree contains 2")

	for number in range(2,10,3):
		print("Removing " + str(number))
		root.remove(number)
	print("Tree with removed nodes:")
	treePrint.printTree(root)
	

def inorderTraversalPrint(node):
	inorderTraversalPrintInternal(node, 0)

def inorderTraversalPrintInternal(node, level):
	if node is None:
		return
	inorderTraversalPrintInternal(node.left, level + 1)
	print "  " * level + str(node.value)
	inorderTraversalPrintInternal(node.right, level + 1)
	
def preorderTraversalPrint(node):
	preorderTraversalPrintInternal(node, 0)

def preorderTraversalPrintInternal(node, level):
	if node is None:
		return
	print "  " * level + str(node.value)
	preorderTraversalPrintInternal(node.left, level + 1)
	preorderTraversalPrintInternal(node.right, level + 1)
	

if __name__ == '__main__':
	main()
