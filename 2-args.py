#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
count = len(argv)
if count == 1:
    print("{} arguments.".format(count - 1))
else:
    if count == 2:
        print("{} argument:".format(count - 1))
    else:
        print("{} arguments:".format(count - 1))
    for i in range(1, count):
        print("{}: {}".format(i, argv[i]))
