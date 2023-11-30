#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)

    i = 0
    while i < len(names):
        name = names[i]
        if name[:2] != "__":
            print(name)
        i += 1
