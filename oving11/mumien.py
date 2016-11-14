from sys import stdin, stderr

def best_path(nm, prob):
    current_node = 0
    updated_weights = [x for x in range(len(nm))] #list to hold updated max_weights
    updated_weights[0] = nm[0][0] #sets the max weight of the start node to the start node
    predecesor_list = [-1 for x in range(len(nm))]
    visited_count = 0

    while nm[len(nm)-1][current_node] != 1 and visited_count < len(nm)-1:
        #iterates until all nodes have been visited or the max node is neighbour to finnish node
        for n in range(len(nm)):
            old_value = updated_weights[n]
            new_value = updated_weights[current_node]*prob[n]
            if new_value > old_value:
                updated_weights[n] =

        updated_weights[current_node] = -1 #this marks every node that has been visited with a negative number
        visited_count += 1






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

