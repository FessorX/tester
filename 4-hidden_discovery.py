#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    file = dir(hidden_4)
    count = len(file)
    for i in range(0, count):
        if file[i][0:2] != "__":
            print(file[i])
