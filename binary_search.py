class BinarySearch():
	def search_iterative(self, list, item):
		low = 0
		high = len(list) - 1;

		while low <= high:
		# ... check the middle element
			mid = (low + high) // 2
			guess = list[mid]
			# Found the item.
			if guess == item:
				return mid
			# The guess was too high.
			if guess > item:
				high = mid - 1
			# The guess was too low.
			else:
				low = mid + 1

		# Item doesn't exist
		return None


if __name__ == "__main__":
  # We must initialize the class to use the methods of this class
	bs = BinarySearch()
	my_list = [1, 3, 5, 7, 9, 12, 13, 20, 25, 78, 101]
  
	print(bs.search_iterative(my_list, 3)) # => 1
	print(bs.search_iterative(my_list, 9)) # => 4
	print(bs.search_iterative(my_list, 78)) # => 9