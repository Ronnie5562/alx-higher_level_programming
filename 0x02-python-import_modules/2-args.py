#!/usr/bin/python3
if __name__ == "__main__":
    """Prints out the CLI arguments."""
    from sys import argv

    index = len(argv) - 1
    if index == 0:
        print("0 arguments.")
    elif index == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(index))
    for i in range(index):
        print("{}: {}".format(i + 1, argv[i + 1]))