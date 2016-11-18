#!/usr/bin/python

import random

# A small implementation of different tree structures in python

def constructRandomBinarySearchTree(values):
	root = BinarySearchTree(values.pop(random.randrange(len(values))))
	while len(values) > 0:
		randomValue = values.pop(random.randrange(len(values)))
		root.insert(randomValue)
	return root

class BinarySearchTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None

	def insert(self, value):
		if value > self.value:
			if self.right is None:
				self.right = BinarySearchTree(value)
				self.right.parent = self
			else:
				self.right.insert(value)
		elif value < self.value:
			if self.left is None:
				self.left = BinarySearchTree(value)
				self.left.parent = self
			else:
				self.left.insert(value)

	def contains(self, value):
		if self.value == value:
			return True
		elif self.value < value:
			return self.right.contains(value)
		elif self.value > value:
			return self.left.contains(value)

	def replaceNode(self, newNode):
		if self.parent:
			if self.parent.left == self:
				self.parent.left = newNode
			else:
				self.parent.right = newNode
		if newNode:
			newNode.parent = self.parent

	def remove(self, value):
		if self.value < value:
			self.right.remove(value)
		elif self.value > value:
			self.left.remove(value)
		else:
			if self.left is None and self.right is None:
				self.replaceNode(None)
			elif self.left and self.right:
				nextValue = self.right.getMin()
				self.value = nextValue.value
				nextValue.remove(nextValue.value)
			elif self.left:
				self.replaceNode(self.left)
			else:
				self.replaceNode(self.right)

	def getMin(self):
		minNode = self
		while minNode.left:
			minNode = minNode.left
		return minNode
