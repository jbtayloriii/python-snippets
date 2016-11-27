#!/usr/bin/python

class minHeap:
	def __init__(self):
		self.size = 0
		self.tree = []

	def add(self, value):
		self.size += 1
		self.tree.append(value)

		#bubble up to satisfy heap
		position = len(self.tree) - 1
		parentPosition = (position - 1) // 2
		while position > 0 and self.tree[position] < self.tree[parentPosition]:
			temp = self.tree[position]
			self.tree[position] = self.tree[parentPosition]
			self.tree[parentPosition] = temp

			position = parentPosition
			parentPosition = (position - 1) // 2

	def peekMin(self):
		if len(self.tree) == 0:
			return None
		else:
			return self.tree[0]

	def getMin(self):
		if len(self.tree) == 0:
			return None

		#swap with last position and remove it
		minValue = self.tree[0]
		self.tree[0] = self.tree[len(self.tree) - 1]
		self.tree.pop()
		
		#bubble down to satisfy heap
		position = 0
		left = (position * 2) + 1
		right = (position * 2) + 2
		
		#This long condition checks that we have children and that we violate heap
		# (position value is greater than either of its children)
		while (left < len(self.tree) and self.tree[position] > self.tree[left]) or (right < len(self.tree) and self.tree[position] > self.tree[right]):
			if (not right < len(self.tree)) or self.tree[left] < self.tree[right]:
				#swap with left
				swap(self.tree, position, left)
				position = left
				left = (position * 2) + 1
				right = (position * 2) + 2
			else:
				#swap with right
				swap(self.tree, position, right)
				position = right
				left = (position * 2) + 1
				right = (position * 2) + 2
		return minValue
	
def swap(array, pos1, pos2):
	value = array[pos1]
	array[pos1] = array[pos2]
	array[pos2] = value
