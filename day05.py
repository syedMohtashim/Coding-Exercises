# ------------------------------------------------------------------------------
# ********************************* { DAY 05 } *********************************
# ------------------------------------------------------------------------------

# QUESTION : Add Two Numbers represented in a linked list.
# Input: l1 = 2 -> 4 -> 4, l2 = 5 -> 6 -> 4
# Output: 8 -> 0 -> 8
# Explanation: {244 + 564 = 808}.

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self,new_data):
		node1 = Node(new_data)
		node1.next = self.head
		self.head = node1



	def add_two_LL(self, l1, l2):
		pass






