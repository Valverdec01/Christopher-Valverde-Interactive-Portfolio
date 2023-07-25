import functions as f

def main():
    f.get_requirement()
    f. estimate_painting_cost()
    choice = str(input('Estimate another paint job? (y/n): '))

    while choice == 'y':
        f.estimate_painting_cost()
        choice = str(input('Estimate another paint job? (y/n): ')) 
    else:

        print("\nThank you for using our Paint Estimator!")
        print("\nPlease see our web site: https://www.linkedin.com/in/christopher-valverde-695b4721b/")

if __name__ == "__main__":
    main()

