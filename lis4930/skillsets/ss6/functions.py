#!/usr/bin/env python3
def get_requirements():
	print("Developer: Christopher Valverde")
	print("Python Looping Structures")
	print("\nProgram Requirements:\n"
		+ "1. Print while loop. \n"
		+ "2. Print for loops using range() function, and implicit and explicit lists. \n"
		+ "3. Use break and continue statements.\n" 
		+ "4. Replicate display below \n")

def print_loops():

	print("1.while loop:")
	i = 1
	while i <=3:
		print(i)

		i = i + 1

	print("\n2. for loop: using range() function with 1 arg:")



	for i in range(4):
		print(i)

	print("\n3. for loop: using range() function with two args:")


	for i in range(1, 4):
		print(i)

	print("\n4. for loop: using range() function with three args (interval 2):")


	for i in range(1, 4, 2):
		print(i)

	print("\n5. for loop: using range() with thre args (negative interval):")


	for i in range (3, 0, -2):
		print(i)

	print("\n6. for loop using (implicit) list (i.e, list not assigned to variable):")

	for i in [1, 2, 3]:
		print(i)

	print("\n7. for loop iterating through (explicit) string list:")
	states = ['Michigan', 'Alabama', 'Florida']
	for state in states:
		print(state)

	print("\n8. for loop using break statement (stops loop): ")
	states = ['Michigan', 'Alabama', 'Florida']
	for state in states:
		if state == "Alabama":
			break
		print(state)

	print("\n9. for loop using continue statement (stops and continues with next): ")
	states = ['Michigan', 'Alabama', 'Florida']
	for state in states:
		if state == "Alabama":
			continue
		print(state)	

	print("\n10. print list length: ")
	states = ['Michigan', 'Alabama', 'Florida']
	print(len(states))

