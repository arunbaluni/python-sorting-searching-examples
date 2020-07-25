# This example covers the concept of Merge Sort implementation

# Merge Sort
def merge_sort(input_list):
	if(len(input_list) > 1):
		mid = len(input_list) // 2

		left_list = input_list[ : mid]
		right_list = input_list[mid : ]

		# Recursion to split the input in equal havles till input list lenght is greater than 1
		merge_sort(left_list)
		merge_sort(right_list)

		iterate_left_list = 0
		iterate_right_list = 0
		iterate_merged_list = 0

		# Compare left_list items with right list items and update the merged list
		while iterate_left_list < len(left_list) and iterate_right_list < len(right_list):
			if (left_list[iterate_left_list]  <  right_list[iterate_right_list]):
				input_list[iterate_merged_list] = left_list[iterate_left_list]
				iterate_left_list += 1
			else:
				input_list[iterate_merged_list] = right_list[iterate_right_list]
				iterate_right_list += 1

			iterate_merged_list += 1

		# Add leftover items in left list to merged list
		while iterate_left_list < len(left_list):
			input_list[iterate_merged_list] = left_list[iterate_left_list]
			iterate_left_list += 1
			iterate_merged_list += 1

		# Add leftover items in right list to merged list
		while iterate_right_list < len(right_list):
			input_list[iterate_merged_list] = right_list[iterate_right_list]
			iterate_right_list += 1
			iterate_merged_list += 1			


def main():
	# Enter the input list to sort

	input_list_array = [ [31, 9, 11, 2, 5 ], [5, 7, 8, 5, 2], [12, 11, 10], [13, 11], [6], [], [239, 132, -61, -31, 0, 45, 1003, 12, 18] ]

	for input_list in input_list_array:
		print("\nInput List for sorting", input_list)
		merge_sort(input_list)
		print("Sorted List", input_list)


if(__name__ == "__main__"):
	main()
