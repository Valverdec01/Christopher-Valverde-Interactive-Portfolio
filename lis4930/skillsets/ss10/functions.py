#!/usr/bin/ env python3

def get_requirements():
    print("Developer: Christopher Valverde")
    print("\nPython Dictionaries")
    print()
    print("Program Requirements:")
    print("1. Dictionaries (Python data structure): unordered key:value pairs.")
    print("2. Dictionary: an associative array (also known as hashes")
    print("3. Any key in a dictionary is associated (or mapped) to a value (i.e., any Python data type.")
    print("4. Keys: must be of immutable type (string, number or tuple with immutable elements) and must be unique.")
    print("5. Values: can be of any data type and can repeat.")
    print("6. Create a program that mirrors the following IPO (input/process/output) format.")
    print("\tCreate empty dictionary, using curly braces \{\}: my_dictionary = \{\}")
    print("\tUse the following keys: fname, lname, degree, major, gpa")
    print("Note: Dictionaries have key-value pairs instead of single values; this differentiates a dictionary from a set.")
    print()

def using_dictionaries():
    print("Input:")
    fname = input("First Name: ")
    lname = input("Last name: ")
    degree = input("Degree: ")
    major = input("Major (IT or ICT): ")
    gpa = input("GPA: ")
    print()

    print("Output:")
    my_dictionary = {"fname": fname, "lname": lname, "degree": degree, "major": major, "gpa": gpa}
    print("Print my_dictionary: ")
    print(my_dictionary)

    print("\nReturn view of dictionary's (key, value) pair, built-in function:")
    print(my_dictionary.items())

    print("\nReturn view object of all keys, built-in function:")
    print(my_dictionary.keys())

    print("\nReturn view object of all values in dictionary, built-in function:")
    print(my_dictionary.values())

    print("\nPrint only first and last names, using keys: ")
    print(my_dictionary['fname'], my_dictionary['lname'])

    print("\nPrint only first and last names, using get() function: ")
    print(my_dictionary.get("fname"), my_dictionary.get("lname"))

    print("\nCount number of item (key: value pairs) in dictionary: ")
    print(len(my_dictionary))

    print("\nRemove last dictionary item (popitem):")
    my_dictionary.popitem()
    print(my_dictionary)

    print("\nDelete major from dictionary, using key:")
    del my_dictionary["major"]
    print(my_dictionary)

    print("\nReturn object type: ")
    print(type(my_dictionary))

    print("\nDelete all items of list: ")
    my_dictionary.clear()
    print(my_dictionary)


def main():
    get_requirements()
    using_dictionaries()
main()