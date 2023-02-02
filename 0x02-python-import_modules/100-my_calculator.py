#!/usr/bin/python3

if __name__ == "__main__":
    """a program that imports all functions from the file calculator_1.py and handles basic operations."""
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) - 1 != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        if sys.argv[1] == '+':
            print(f'{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {add(int(sys.argv[1]), int(sys.argv[3]))}')
        elif sys.argv[1] == '-':
            print(f'{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {sub(int(sys.argv[1]), int(sys.argv[3]))}')
        elif sys.argv[1] == '*':
            print(f'{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {mul(int(sys.argv[1]), int(sys.argv[3]))}')
        elif sys.argv[1] == '/':
            print(f'{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {div(int(sys.argv[1]), int(sys.argv[3]))}')
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)
