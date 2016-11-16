#!/usr/bin/python

import sys

def printTree(root):
	indentList = []
	getNodeIndentations(root, indentList, 0, 0)
	printIndentList(indentList)

#not used, but is built upon in getNodeIndentations
def getNodeSpace(node):
	if node is None:
		return 0
	valueSpace = len(str(node.value))
	leftSpace = getNodeSpace(node.left)
	rightSpace = getNodeSpace(node.right)
	return leftSpace + rightSpace + valueSpace

#returns None for null node or a tuple of (leftIndent (where to start drawing the value), totalSizeOfTree)
#this method assumes that whatever you are printing this to has enough horizontal room to accomodate the tree
#If you extend beyond 80 characters for the tree (around 35 nodes for a simple range of 1-35), you will get wrapping
def getNodeIndentations(node, indentList, level, preindent):
	if node is None:
		return None

	#add two internal lists for each level (one for the numbers, one for the edges)
	if len(indentList) < level + 1:
		indentList.append([])
		indentList.append([])
	
	leftIndent = rightIndent = 0

	#For each recursive call, we want to get the indentation for the child value + edge, and the total space it takes
	#The edges will go in a separate line, so we descend two "levels" for the sake of drawing the tree for each
	#single level in the tree
	leftTuple = getNodeIndentations(node.left, indentList, level + 2, preindent)
	if not leftTuple is None:
		leftIndent = leftTuple[1]
		indentList[level + 1].append(['/', preindent + leftTuple[0]])

	valueSize = len(str(node.value))
	indentList[level].append([node.value, preindent + leftIndent])

	rightTuple = getNodeIndentations(node.right, indentList, level + 2, preindent + leftIndent + valueSize)
	if not rightTuple is None:
		rightIndent = rightTuple[1]
		indentList[level + 1].append(['\\', preindent + leftIndent + valueSize + rightTuple[0]])	

	return [leftIndent, leftIndent + valueSize + rightIndent]
		
def printIndentList(list):
	for sublist in list:
		space = 0
		for value in sublist:
			preIndent = value[1] - space
			sys.stdout.write(" " * preIndent + str(value[0]))
			space = space + preIndent + len(str(value[0]))
		print("")
