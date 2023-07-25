def get_requirements():
	print("Developer: Christopher Valverde")
	print("Calorie Percentage")
	print("\nProgram Requirements:\n"
		+ "1. Find calories per grams of fat, carbs, and protein. \n"
		+ "2. Calculate percentages. \n"
		+ "3. Must use float data types.\n" 
		+ "4. Format, right-align numbers, and round to two decimal places. \n")

def get_user_input():
	
	fat_grams = 0.0
	carb_grams = 0.0
	protein_grams = 0.0

	print("Input:")
	fat_grams = float(input("Enter total fat grams: "))
	carb_grams = float(input("Enter total carb grams: "))
	protein_grams = float(input("Enter total carb grams: "))

	return fat_grams, carb_grams, protein_grams


def calculate_calories(f_grams, c_grams, p_grams):

	total_calories = 0.0
	percent_fat = 0.0
	percent_carbs = 0.0
	percent_protein = 0.0



	calories_from_fat = f_grams * 9
	calories_from_carbs = c_grams * 4
	calories_from_protein = p_grams * 4
	total_calories = calories_from_fat + calories_from_carbs + calories_from_protein


	percent_fat = calories_from_fat / total_calories
	percent_carbs = calories_from_carbs / total_calories
	percent_protein = calories_from_protein / total_calories








	print("\nOutput:")
	print("{0:8} {1:>10} {2:>13}".format("Type","Calories","Percentage"))

	print("{0:8} {1:10,.2f} {2:13.2%}".format(
		"Fat", calories_from_fat, percent_fat))

	print("{0:8} {1:10,.2f} {2:13.2%}".format(
		"Carbs", calories_from_carbs,percent_carbs))

	print("{0:8} {1:10,.2f} {2:13.2%}".format(
		"Protein", calories_from_protein, percent_protein))
