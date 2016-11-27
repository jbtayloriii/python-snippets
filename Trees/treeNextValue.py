#!usr/bin/python

def getNextSequentialBinarySearchTreeNode(node):
	if node.right:
		n = node.right
		while n.left:
			n = n.left
		return n
	else:
		n = node
		while n.parent and n.parent.right == node:
			n = n.parent
		if not n.parent:
			return None #We are the last node, there is no sequential node
		else:
			return n.parent
