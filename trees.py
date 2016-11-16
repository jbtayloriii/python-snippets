#!/usr/bin/python

# A small implementation of different tree structures in python

class BinarySearchTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		if value > self.value:
			if self.right is None:
				self.right = BinarySearchTree(value)
			else:
				self.right.insert(value)
		elif value < self.value:
			if self.left is None:
				self.left = BinarySearchTree(value)
			else:
				self.left.insert(value)

