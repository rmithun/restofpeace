'''
author : mithun

'''

### this is a basic stack with push ,pop ,isEmpty methods ###

class myStack:
   def __init__(self):
	self.container = []
   def isEmpty(self):
	return self.size() == 0
   def push(self,item):
	self.container.append(item)
   def pop(self):
	return self.container.pop(-1)
   def size(self):
	return len(self.container)
