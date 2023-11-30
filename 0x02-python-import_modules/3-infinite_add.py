#!/usr/bin/python3
import sys

if __name__ == "__main__":
    s = 0

    i = 1
    while i < len(sys.argv):
        s += int(sys.argv[i])
        i += 1

    print("{}".format(s))
