"""
File: name_sq.py (extension)
Name: Sanny Lin
----------------------------
(Instructions by stanCode)
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main():
    """
    function: make a square pattern, which is circled by the inputted name
    """
    print("This program prints a name in a square pattern!")
    name = input("Name: ")
    my_name_pattern(name)


def my_name_pattern(name):
    """
    function: district the pattern into 3 parts, print in sequence
    (1) name
    (2) vertical words
    (3) name in reverse order
    """
    # part(1): name
    print(str(name))
    # part(2): vertical words
    for i in range(1, len(name)-1):
        print(name[i], end="")
        for j in range(len(name)-2):
            print(" ", end="")
        print(name[len(name)-i-1])
    # part(3): name in reverse order
    for i in range(len(name)):
        print(name[len(name)-i-1], end="")


if __name__ == '__main__':
    main()
