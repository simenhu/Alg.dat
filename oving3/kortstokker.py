#!/usr/bin/python3

from sys import stdin
from itertools import repeat




def merge(decs):
    returnstring = ""

    while True:
        min_index = 0
        for i in range(len(decs)):
            if decs[i][0][0] < decs[min_index][0][0]:
                min_index = i
        returnstring += decs[min_index][0][1]
        del decs[min_index][0]
        if len(decs[min_index])==0:
            del decs[min_index]


        if len(decs)==0:
            return returnstring


def main():
    decks = [list(zip(map(int, line.strip().split(':')[1].split(',')), repeat(line.strip().split(':')[0]))) for line in stdin]
    print(merge(decks))


if __name__ == "__main__":
    main()

[list(zip(map(int, line.strip().split(':')[1].split(',')), repeat(line.strip().split(':')[0]))) for line in stdin]
