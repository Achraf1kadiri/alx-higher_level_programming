#!/usr/bin/python3
def uppercase(string):
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{0}".format(char), end="")
    print("")
