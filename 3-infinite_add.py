#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = len(argv)
    sum = 0
    for i in range(1, count):
        sum += argv[i]
    print(sum)
