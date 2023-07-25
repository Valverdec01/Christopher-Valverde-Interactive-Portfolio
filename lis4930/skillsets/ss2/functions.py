def get_requirements():
	print("Developer: Christopher Valverde")
	print("Miles Per Gallon")
	print("\nProgram Requirements:\n"
	+ "1. Convert MPG. \n"
	+ "2. Must use float data type for user input and calculation.\n"
	+ "3. Format and round conversion to two decimal places. \n")

def calculate_miles_per_gallon():
	miles = 0.0
	gallons = 0.0
	mpg = 0.0

	print("Input:")
	miles = float(input("Enter miles driven: ")) 
	gallons = float(input("Enter gallons of fuel used: "))

	mpg = miles / gallons


	print("\nOutput:")
	print("{0:,.2f} {1} {2:,.2f} {3} {4:,.2f} {5}".format(
		miles, "miles driven and", gallons, "gallons used =", mpg, "mpg"))


