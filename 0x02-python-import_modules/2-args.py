#!/usr/bin/python3
if __name__ == "__main__":
    """Prints out the CLI arguments."""
    from sys import argv

    if len(argv) == 0:
        print("0 arguments.")
    elif len(argv) == 1:
        print("1 argument:")
    else:
       print("{} arguments:".format(len(argv)))
    if len(argv) != 0:
        for index in range(len(argv) - 1):
            print("{}: {}".format(index + 1, argv[index + 1]))