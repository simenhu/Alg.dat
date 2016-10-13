#!/usr/bin/python3

from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict

strings = ['kobra', 'alge', 'agg', 'kort', 'hyblen']
d = 6
def flexradix(A, d):
    for i in reversed(range(0,d)):
        buckets = [[] for x in range(123)]
        for n in A:
            if i > len(n)-1:
                buckets[96].append(n)
            else:
                buckets[ord(n[i])].append(n)
        A = [x for y in buckets for x in y]
    return A


def main():
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        strings.append(line.rstrip())
    A = flexradix(strings, d)
    for string in A:
        print(string)


if __name__ == "__main__":
    main()
    #A = flexradix(strings, d)
    #for string in A:
    #    print(string)
