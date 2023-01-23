#!/usr/bin/python3
if __name__ == "__main__":
    """Prints out the CLI arguments."""
    from sys import argv

    x = len(argv) - 1
    if x == 0:
        print("0 arguments.")
    elif x == 1:
        print("1 argument:")
    else:
       print("{} arguments:".format(x))
    for index in range(x):
        print("{}: {}".format(index + 1, argv[index + 1]))