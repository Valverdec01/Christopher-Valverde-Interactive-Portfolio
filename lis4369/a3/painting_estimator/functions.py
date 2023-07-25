# Developer: Christopher Valverde

# Course: LIS4369

# Semester: Fall 2022

# Program requirements:
def get_requirement():
    print("Painting Estimator")
    print("\nProgram Requirements:\n"
    + "1. Calculate home interior paint cost (w/o primer) \n"
    + "2. Must use float data types.\n"
    + "3. Must use SQFT_PER_GALLON constant (350).\n"
    + "4. Must use iteration structure (aka ""loop"").\n"
    + "5. Format, right-align numbers, and round to two decimal places.\n"
    + "6. Create at least five functions that are called by the program:\n"
    + "5. Create at least three functions that are called by the program:\n" 
        + "\ta. main(): calls two other functions: get_requirements() and estimate_painting cost(),\n"
        + "\tb. get_requirements(): displays the program requirements.\n"
        + "\tc. estimate_painting_cost(): calculates interior home painting, and calls print functions, \n"
        + "\td. print painting_estimate(): displays painting costs. \n"
        + "\te. print_painting percentage(): displays painting costs percentages.\n")

def estimate_painting_cost():
    
    sqFtGallon = 350.00
    print("Input: ")
    interior = float(input('Enter total interior sqft: '))
    gallonPrice = float (input('Enter price per gallon paint: '))
    hourlyRate = float(input('Enter hourly painting rate per sq ft: '))
    numGallon = interior / sqFtGallon
    print_painting_estimate(interior, sqFtGallon, numGallon, gallonPrice, hourlyRate)

    print_painting_percentage(interior, sqFtGallon, numGallon, gallonPrice, hourlyRate)

def print_painting_estimate(sqFtTotal, sqFtGallon, numGallon, paintGallon, labor):
    print("\nOutput: ")
    print("Item" + "{0:>31}". format("Amount"))
    print("{0:<10} {1:>10,.2f}". format('Total sq ft:\t\t', sqFtTotal))
    print("{0:<10} {1:>10,.2f}".format('Sq Ft per Gallon: it', sqFtGallon))
    print("{0:<10} {1:>10,.2f}". format( 'Number of Gallons:\t', numGallon))
    print("{0:<10} ${1:>9,.2f}". format('Paint per Gallon:\t', paintGallon))
    print("{0:<10} ${1:>9,.2f}". format('Labor per Sq Ft:\t', labor))

def print_painting_percentage(sqFtTotal, SqFtGallon, numGallon, paintGallon, labor):
    totalPercent = 100.00
    paint = numGallon * paintGallon
    laborCost = labor * sqFtTotal
    total = paint + laborCost
    paintPercent = (paint / total ) * 100 
    laborPercent = (laborCost / total ) * 100

    print("\nCost\t\t Amount\t Percentage ") 
    print("{0:<10} ${1:>10,.2f} {2:>10,.2f}%". format('Paint:\t', paint, paintPercent))
    print("{0:<10} ${1:>10,.2f} {2:>10,.2f}%". format('Labor:\t', laborCost, laborPercent)) 
    print("{0:<10} ${1:>10,.2f} {2:>10,.2f}%". format('Total:\t', total, totalPercent))

def main():
    get_requirement()

    estimate_painting_cost()
    choice = str(input('Estimate another paint job? (y/n): '))

    while choice == 'y':
        estimate_painting_cost()
        choice = str(input('Estimate another paint job? (y/n): ')) 
    else:

        print("\nThank you for using our Paint Estimator!")
    if __name__ == "__main__":
        main()
