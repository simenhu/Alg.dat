#!/usr/bin/python3

from sys import stdin

widths, heights, values, paper_width, paper_height = [2, 2, 4], [3, 3, 5], [5, 4, 16], 20, 20

def max_simen(*args):
    value = 0
    for a in args:
        if a>value:
            value = a
    return value

def max_value(widths, heights, values, paper_width, paper_height):
    #this ensures that the paper is always laying on its longest side
    if paper_height>paper_width:
        paper_height, paper_width = paper_width, paper_height

    #makes an array to store the sub problems
    max_values = [[0 for y in range(paper_width+1)] for x in range(paper_width+1)]

    w = 1 #start iterating with width index = 1
    for h in range(1,paper_height+1): #iterates from height = 1 to height = the height of the paper

        while w <= paper_width: #iterates until w is higher than the width of the paper
            q = 0 #variable to hold the max value for this sub problem
            for seddel in range(len(widths)): #iterates through the seddels to find the best match
                seddel_width, seddel_height = widths[seddel], heights[seddel] #stores the width and height for the current seddel

                #here the seddel lay flatt
                if w>=seddel_width and h>=seddel_height:#this chacks if the seddel fits in the original orientation
                    #this is the scenario where we cut the paper vertical
                    w1, h1 = w-seddel_width, h
                    w2, h2 = seddel_width, h - seddel_height

                    #this is where we cut the paper vertical
                    w3, h3 = w - seddel_width, seddel_height
                    w4, h4 = w, h - seddel_height

                    q = max(q, max_values[w1][h1]+max_values[w2][h2]+values[seddel],
                            max_values[w3][h3]+max_values[w4][h4]+values[seddel])

                #here the seddel stand up
                seddel_width, seddel_height = seddel_height, seddel_width #here we switch the height and width of the seddel to rotate it 90 degrees
                if w >= seddel_width and h >= seddel_height:
                    # this is the scenario where we cut the paper vertical
                    w1, h1 = w - seddel_width, h
                    w2, h2 = seddel_width, h - seddel_height

                    # this is where we cut the paper vertical
                    w3, h3 = w - seddel_width, seddel_height
                    w4, h4 = w, h - seddel_height

                    q = max(q, max_values[w1][h1] + max_values[w2][h2] + values[seddel],
                            max_values[w3][h3] + max_values[w4][h4] + values[seddel])
            max_values[w][h] = q
            max_values[h][w] = q

            w += 1

        w = h+1

    return max_values[paper_width][paper_height]



def test():
    print(max_value(widths, heights, values, paper_width, paper_height))


def main():
    widths = []
    heights = []
    values = []
    for triple in stdin.readline().split():
        dim_value = triple.split(':', 1)
        dim = dim_value[0].split('x', 1)
        width = int(dim[0][1:])
        height = int(dim[1][:-1])
        value = int(dim_value[1])
        widths.append(int(width))
        heights.append(int(height))
        values.append(int(value))
    for line in stdin:
        paper_width, paper_height = [int(x) for x in line.split('x', 1)]
        print((max_value(widths, heights, values, paper_width, paper_height)))


if __name__ == "__main__":
    test()