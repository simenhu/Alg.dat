#!/usr/bin/python3


from sys import stdin



def sort_list(A):
    A_max = max(A)
    A_length = len(A)
    c = [0 for x in range(A_max+1)]
    b = [0 for x in range(A_length)]
    for i in range(A_length):
        c[A[i]] += 1
    for i in range(1, A_max+1):
        c[i] = c[i] + c[i-1]
    for i in range(A_length-1, -1, -1):
        b[c[A[i]]-1] = A[i]
        c[A[i]] -= 1
    return b




def find(A, lower, upper):
    L = 0
    U = len(A)-1
    is_Finished = False
    while not is_Finished:
        if A[L+1]<= lower:
            L+=1

        else:
            is_Finished = True


    is_Finished = False

    while not is_Finished:
        if A[U-1] >= upper:
            U = U - 1

        else:
            is_Finished = True


    return (A[L],A[U])

def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))

    sorted_list = sort_list(input_list)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()

