#!/usr/bin/env python3
import random

def get_requirements():
    print("Developer: Christopher Valverde")
    print("\nPseudo-Random Number Generator")
    print()
    print("Program Requirements:")
    print("1. Get user beginning and ending integer values, and store in two variables.")
    print("2. Display 10 psuedo-random numbers between, and including, above values")
    print("3. Must use integer data types")
    print("4. Example 1: Using range() and randint() functions.")
    print("5. Example 2: Using a list with range() and shuffle() functions.")
    print()

def get_rng():
    print("Input:")
    start = int(input("Enter beginning value: "))
    end = int(input("Enter ending value: "))


    my_sequence = range(6)
    for item in my_sequence:
        print(item)

    print("\nOutput:")
    print("Example 1: Using range() and randint() functions:")
    
    for item in range(10):
        print(random.randint(start, end), sep= ", ", end = " ")

    print()

    print("\nExample 2: Using a list, with range() and shuffle() functions:")
    my_list = list(range(start, end + 1))
    random.shuffle(my_list)
    for item in my_list:
        print(item, sep=", ", end = " ")

    print()

def main():
    get_requirements()
    get_rng()
main()