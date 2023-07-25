#!/usr/bin/env python3
def get_requirements():
	print("Developer: Christopher Valverde")
	print("Python Tuples")
	print("\nProgram Requirements:\n"
		+ "1. Tuples (Python data structure): *immutable* (cannot be changed), orded sequence of elements.\n" 
		+ "2. Tuple are immutable/unchangeable--that is, cannot insert, update, delete.\nNote: can reassign or delete an *entire* tuple--but, *not individual items or slices.\n"
		+ '3. Create tuple using parenthesis (tuple): my_tuple1 = ("cherries", "apples", "bananas", "oranges")\n'
		+ '4. Create tuple (packing), that is,*without* using paranthesis (aka tuple \"packing\"): my_tuple2 = 1, 2, *three*,"four"\n'
		+ '5. Python tuple (unpacking), that is, assign values from tuple to sequence of variables: fruit1, fruit2, fruit3, fruit4 = my_tuple1\n'
		 + "6. Create a program that mirrors the following IPO (input/process/output).\n")


def using_tuples():

	print("\nInput: Hard coded--no user input.")

	my_tuple1 = ("cherries", "apples", "bananas", "oranges")




	my_tuple2 = 1, 2, "three", "four"


	print("\nOutput:")
	print("Print my_tuple1:")
	print(my_tuple1)

	print()

	print("Print my_tuple2:")
	print(my_tuple2)

	print()

	fruit1, fruit2, fruit3, fruit4 = my_tuple1
	print("Print my_tuple1 unpacking:")
	print(fruit1, fruit2, fruit3, fruit4)

	print()
	print("Print \"slice\" of my_tuple1 (second and third elements):")
	print(my_tuple1[1:3])

	print()
	print("Reassign my_tuple2 using paranthesis.")
	my_tuple2 = (1, 2, 3, 4)
	print("Print my_tuple2:")
	print(my_tuple2)

	print()
	print("Reassign my_tuple2 using \"packing\" method (no parantheses).")
	my_tuple2 = 5, 6, 7, 8

	print("Print my_tuple2:")
	print(my_tuple2)

	print()
	print("Print number of elements in my_tuple1: " + str(len(my_tuple1)))



	print()
	print("Delete my_tuple1: ")
	del my_tuple1

	