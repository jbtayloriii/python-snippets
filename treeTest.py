#!/usr/bin/python

import trees
import treePrint
import random

def main():
	root = constructRandomTree()
	treePrint.printTree(root)
		
def constructRandomTree():
	treeValueList = range(1,15)
	root = trees.BinarySearchTree(treeValueList.pop(random.randrange(len(treeValueList))))
	while len(treeValueList) > 0:
		randomValue = treeValueList.pop(random.randrange(len(treeValueList)))
		root.insert(randomValue)
	return root
	

def inorderTraversalPrint(node):
	inorderTraversalPrintInternal(node.right, 1)
	print node.value
	inorderTraversalPrintInternal(node.left, 1)

def inorderTraversalPrintInternal(node, level):
	if node is None:
		return
	inorderTraversalPrintInternal(node.right, level + 1)
	print "  " * level + str(node.value)
	inorderTraversalPrintInternal(node.left, level + 1)
	
def preorderTraversalPrint(node):
	print node.value
	POTPrintInternal(node.right, 1)
	POTPrintInternal(node.left, 1)

def POTPrintInternal(node, level):
	if node is None:
		return
	print "  " * level + str(node.value)
	POTPrintInternal(node.right, level + 1)
	POTPrintInternal(node.left, level + 1)
	

if __name__ == '__main__':
	main()
