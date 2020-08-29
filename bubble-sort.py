# Bubble Sorting

def bubble_sort(input_list):
	pass_value = 0
	for x in range(len(input_list) - 1, 0, -1):
		for y in range(x):
			if(input_list[y] > input_list[y + 1]):
				temp = input_list[y + 1]
				input_list[y + 1] = input_list[y]
				input_list[y] = temp
			else:
				continue
		pass_value += 1
		print("Current sorted list in pass {} is {}: ".format(pass_value, input_list))


def main():
        input_list = []
        input_list_length = int(input("Enter length of list to be created: "))
        for i in range(0, input_list_length, 1):
            temp = int(input("Enter the item " + str(i) + "\n"))
            input_list.append(temp)
        print("##########################\n")
        print("Input list to be sorted:")
        print(input_list, "\n")
        bubble_sort(input_list)
        print("\n\nFinal sorted list:", input_list)
        print("##########################")


if(__name__=="__main__"):
	main()
