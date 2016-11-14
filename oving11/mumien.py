from sys import stdin, stderr

def best_path(nm, prob):
    pass

n = int(stdin.readline())
probabilities = [float(x) for x in stdin.readline().split()]
neighbour_matrix = []
for line in stdin:
    neighbour_row = [0] * n
    neighbours = [int(neighbour) for neighbour in line.split()]
    for neighbour in neighbours:
        neighbour_row[neighbour] = 1
    neighbour_matrix.append(neighbour_row)
print(neighbour_matrix)
print(probabilities)
#print (best_path(neighbour_matrix, probabilities))

