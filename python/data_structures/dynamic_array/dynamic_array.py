# dynamic array implementation
# DA is really a fixed size array that grows its size when the fixed size array is full
# create a fixed size array with length 5, [0,0,0,0,0] -> length 5
# insert 4 elements [1,2,3,4,0]
# insert 5th element [1,2,3,4,5]
# insert 6th element, but the size is full. Let's double it by create a new array of size 10 [0,0,0,0,0,0,0,0,0,0]
# copy over the elements from the old array to the new one. [1,2,3,4,5,0,0,0,0,0]
# do the same process for insert whenever there is no space in the array

import array

class DynamicArray:
	def __init__(self):
		self.size = 5 
		self.arr = array.array("i", (0,)*5) 
		self.pointer = 0
		self.count = 0

	def append(self, data: int) -> None:
		if self.size is self.count:
			# create a new array with double the size of the old array
			new_size = self.size * 2
			new_arr = array.array("i", (0,)*new_size)
			print("new_arr", new_arr)
			# copy over the items from the old array to the new array
			for i in range(self.size):
				new_arr[i] = self.arr[i]
			self.arr = new_arr
			self.size = new_size
			self.arr[self.pointer] = data
			self.pointer += 1
			self.count += 1
			return
		try:
			self.arr[self.pointer] = data
			self.pointer += 1
			self.count += 1
		except Exception as e:
			print("Invalid type")

	def pop(self) -> None:
		if self.count == 0:
			raise Exception(IndexError.__doc__)
		popped_element = self.arr[self.pointer - 1]
		print("popped element", popped_element)
		self.arr[self.pointer - 1] = 0
		self.pointer -= 1
		self.count -= 1

	def remove(self, item: int) -> None:
		# item: to be removed from the array
		if self.count == 0:
			raise Exception(IndexError.__doc__) # raise an exception if the array is empty
		# check if the element is present at the 0th index
		if self.arr[0] == item:
			if self.count == 1: # only one element in the array
				self.arr[0] = 0
				self.pointer -= 1
				self.count -= 1
			else:
				items_to_the_right = self.arr[1:]
				self.arr = items_to_the_right
				self.pointer -= 1
				self.count -= 1
		elif self.arr[self.pointer - 1] == item: # item is present at the last
			self.pop()
		else:
			# item is somewhere in middle
			found = False
			for index, value in enumerate(self.arr): # iterating an enumerate object returns both index and value
				if value == item:
					found = True
					items_to_the_left = self.arr[0:index]
					items_to_the_right = self.arr[index+1:]
					self.arr = items_to_the_left + items_to_the_right # merges both array
					self.pointer -= 1
					self.count -= 1
			if not found:
				print(f"{item} not found in the array")

	def __repr__(self):
		return f"{self.arr}, size: {self.size}, pointer: {self.pointer}, count: {self.count}"



if __name__ == "__main__":
	da = DynamicArray()
	print(da)
	for i in range(5):
		da.append(i)
	print(da)
	for i in range(6, 11):
		da.append(i)
	print(da)
	da.append(11)
	print(da)
	da.append(12)
	print(da)
	da.pop()
	print(da)
	da.pop()
	print(da)
	da.pop()
	print(da)
	da.pop()
	print(da)
	for _ in range(8):
		da.pop()
	print(da)
	# da.pop() # uncomment this to crash the program due to IndexError
	for i in range(1,7):
		da.append(i)
	print(da)
	da.remove(1)
	print(da)
	da.remove(6) # since 6 is the last element in the array internally it uses pop method to remove it.
	print(da)
	da.remove(3)
	print(da)
	da.remove(4)
	print(da)
	da.remove(2)
	print(da)
	da.remove(100)
	print(da)
	da.remove(5)
	print(da)
	da.remove(6) # should crash the program by throwing IndexError
	print(da)

