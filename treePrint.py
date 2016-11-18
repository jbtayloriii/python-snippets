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

	#add another level if we haven't reached it yet
	if len(indentList) < level + 1:
		indentList.append([])
	
	#For each recursive call, we want to get the space that each child takes up as well as where that direct
	#child node is placed

	leftIndent = rightIndent = 0

	leftSide = getNodeIndentations(node.left, indentList, level + 1, preindent)
	if not leftSide is None:
		leftChildPosition = leftSide[0]
		leftIndent = leftSide[1]

	nodeSize = len(str(node.value))

	rightSide = getNodeIndentations(node.right, indentList, level + 1, preindent + leftIndent + nodeSize)
	if not rightSide is None:
		rightChildPosition = rightSide[0] + leftIndent + nodeSize
		rightIndent = rightSide[1]

	if node.left and node.right:
		#position us halfway between our children
		nodePosition = (leftChildPosition + rightChildPosition) // 2
	else:
		nodePosition = leftIndent

	#save the absolute node position, its value, and its child node positions
	info = nodeInfo(nodePosition + preindent, node.value)
	if node.left:
		info.leftPosition = preindent + leftChildPosition
	if node.right:
		info.rightPosition = preindent + rightChildPosition
	indentList[level].append(info)

	return [nodePosition, leftIndent + nodeSize + rightIndent]
		
def printIndentList(list):
	for sublist in list:
		usedSpace = 0
		for node in sublist:
			leftEdgeAmount = 0
			if not node.leftPosition is None:
				leftSpace = node.leftPosition - usedSpace + 1
				leftEdgeAmount = node.nodePosition - node.leftPosition - 1
			else:
				leftSpace = node.nodePosition - usedSpace

			sys.stdout.write(" " * leftSpace + "_" * leftEdgeAmount + str(node.value))
			usedSpace = usedSpace + leftSpace + leftEdgeAmount + len(str(node.value))

			if not node.rightPosition is None:
				rightEdgeAmount = node.rightPosition - node.nodePosition - len(str(node.value))
				sys.stdout.write("_" * rightEdgeAmount)
				usedSpace = usedSpace + rightEdgeAmount
		print("")

		#print diagonal edges in between rows now
		secondRowIndent = 0
		for node in sublist:
			if not node.leftPosition is None:
				leftSpace = node.leftPosition - secondRowIndent
				sys.stdout.write(" " * leftSpace + '/')
				secondRowIndent = secondRowIndent + leftSpace + 1
			if not node.rightPosition is None:
				rightSpace = node.rightPosition - secondRowIndent
				sys.stdout.write(" " * rightSpace + '\\')
				secondRowIndent = secondRowIndent + rightSpace + 1
		print("")

class nodeInfo:
	def __init__(self, nodePosition, value):
		self.value = value
		self.nodePosition = nodePosition
		self.leftPosition = None
		self.rightPosition = None
				
