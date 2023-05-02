# Name: Kieren Williamson
# Class: Comp 163-001
# Date: March 24, 2023,
# Description: A simple calculator that uses handmade functions to perform math operations that normally one could use
# the math module for

import kjwilliamson_MyMath as Math


def simple_calc():
    print("Kieren Williamson")
    print('Comp 163')
    print("Simple Calc")
    print("")


def display_menu():
    print("A) add")
    print("S) subtract")
    print("M) multiply")
    print("D) divide")
    print("P) power")
    print("L) LCM")
    print("G) GCD")
    print("R) root")
    print("SS) sine")
    print("C) cosine")
    print("T) tangent")
    print("Q) Quit")
    print()


def display_menu_error():
    return "Invalid menu selection"


# declarations
validMenuLetters = ("A", "S", "M", "D", "Q", "P", "L", "G", "R", "SS", "C", "T")
validDivChoices = ('ID', 'SD', 'Q')
simple_calc()

# displays input validation; user knows that they entered the wrong number because we give a response to their input
while True:
    display_menu()
    menuChoice = input("Menu Selection: ").upper()
# The trig functions only take one argument, so I made sure to put them at the top of the if/elif tree and underneath
# them place the prompt for that argument. Along with a re-prompting of the menu
    if menuChoice not in validMenuLetters:
        print(display_menu_error())
    if menuChoice == 'Q':
        break
    if menuChoice == 'SS':
        trigOp = float(input('Enter your operand in radians: '))
        print(f'The sine of {trigOp} radians is {Math.sine(trigOp)}')
        print()
        display_menu()
        menuChoice = input("Menu Selection: ").upper()
    elif menuChoice == 'C':
        trigOp = float(input('Enter your operand in radians: '))
        print(f'The cosine of {trigOp} radians is {Math.sine(trigOp)}')
        print()
        display_menu()
        menuChoice = input("Menu Selection: ").upper()
    elif menuChoice == 'T':
        trigOp = float(input('Enter your operand in radians: '))
        print(f'The tangent of {trigOp} radians is {Math.sine(trigOp)}')
        print()
        display_menu()
        menuChoice = input("Menu Selection: ").upper()
    op1 = float(input('Enter your operand: '))
    op2 = float(input('Enter your operand: '))
    if menuChoice == 'A':
        print(f'The sum of {op1} and {op2} is {Math.calc_add(op1, op2)}\n')
    elif menuChoice == 'S':
        print(f'The difference between {op1} and {op2} is {Math.calc_subtract(op1, op2)}\n')
    elif menuChoice == 'M':
        print(f'The product of {op1} and {op2} is {Math.calc_multiply(op1, op2)}\n')
    elif menuChoice == 'D':
        divisionChoice = input('Would you like to perform Integer Division(ID), Standard Division(SD), or Q to quit: ').upper()
        if divisionChoice not in validDivChoices:
            print(display_menu_error())
        elif divisionChoice == 'Q':
            break
        elif divisionChoice == 'ID':
            print(f'The quotient of {op1} and {op2} is {Math.floorDiv(op1, op2)}\n')
        elif divisionChoice == 'SD':
            print(f'The quotient of {op1} and {op2} is {Math.calc_divide(op1, op2)}\n')
    elif menuChoice == 'P':
        if op2 == 1:
            print(f'{op1} raised to the 1st power is {Math.power(int(op1), int(op2))}\n')
        elif op2 == 0:
            print(f'{op1} raised to the 0 power is {Math.power(int(op1), int(op2))}\n')
        elif op2 == 2:
            print(f'{op1} raised to the 2nd power is {Math.power(int(op1), int(op2))}\n')
        elif op2 == 3:
            print(f'{op1} raised to the 3rd power is {Math.power(int(op1), int(op2))}\n')
        else:
            print(f'{op1} raised to the {op2}th power is {Math.root(op1, op2)}\n')
    elif menuChoice == 'L':
        print(f'The least common multiple between {op1} and {op2} is {Math.lcm(int(op1), int(op2))}')
    elif menuChoice == 'G':
        print(f'The greatest common divisor between {op1} and {op2} is {Math.gcd(int(op1), int(op2))}')
    elif menuChoice == 'R':
        if op2 == 1:
            print(f'The first root of {op1} is {Math.root(op1, op2)}')
        elif op2 == 2:
            print(f'The second root of {op1} is {Math.root(op1, op2)}')
        elif op2 == 3:
            print(f'The third root of {op1} is {Math.root(op1, op2)}')
        else:
            print(f'The {op2}th root of {op1} is {Math.root(op1, op2)}')
