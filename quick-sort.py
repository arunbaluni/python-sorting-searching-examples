# This covers the implementation of Quick Sort
# Benefits
	# Complexity - O(n Log n)
	# In place data - No extra memory required
	# Worst performance - O(n^2) - When input list or array is already sorted

class QuickSort:

	def quick_sort(self, dataset, low, high):
		if low < high:
			partition_index = self.partition_function(dataset, low, high)

			self.quick_sort(dataset, low, partition_index - 1)
			self.quick_sort(dataset, partition_index + 1, high)

	def partition_function(self, dataset, low, high):
		pivot_value = dataset[low]
		i = low +  1
		j = high

		done = False

		while not done:
			while i <= j and dataset[i] <= pivot_value:
				i += 1

			while dataset[j] >= pivot_value and j >= i:
				j -= 1

			if j < i:
				done = True
			else:
				temp_1 = dataset[j]
				dataset[j] = dataset[i]
				dataset[i] = temp_1

		temp_2 = dataset[low]
		dataset[low] = dataset[j]
		dataset[j] = temp_2

		return j

def main():
	# Inputs to test the quick sort algorithm
	input_list_array = [ [31, 9, 11, 2, 5 ], [5, 7, 8, 5, 2], [12, 11, 10], [13, 11], [6], [], [239, 132, -61, -31, 0, 45, 1003, 12, 18] ]

	quickSort = QuickSort()

	for input_list in input_list_array:
		print("\nInput List for sorting", input_list)
		quickSort.quick_sort(input_list, 0, len(input_list)-1)
		print("Sorted List", input_list)

if(__name__ == "__main__"):
	main()